import base64
import hashlib
import hmac
import random
import typing

from torcontrol.async_connection import ControlProtocol, create_connection, create_unix_connection
from torcontrol.base import AuthMethod, TorSignal, ServerSpec, CircuitPurpose, RouterPurpose, CloseStreamReason, \
    TorFeature, ProtocolInfo
from torcontrol.errors import TorException, TorProtocolException
from torcontrol.events import EventDispatcher
from torcontrol.onion_builder import OnionBuilderV3, OnionBuilderV2
from torcontrol.protocol import Response
from torcontrol.utils import qs

DEFAULT_AUTH_METHODS = (AuthMethod.SAFE_COOKIE, AuthMethod.COOKIE, AuthMethod.HASHED_PASSWORD, AuthMethod.NULL)


class AsyncConnection:
    def __init__(self, protocol: ControlProtocol):
        self._protocol = protocol
        self.timeout = None
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    def close(self):
        self._protocol.close()

    @property
    def is_closed(self):
        return self._protocol.is_closed

    async def _send(self, *data: str, body: str = None) -> Response:
        return await self._protocol.request(*data, body=body, timeout=self.timeout)

    async def _sc(self, *args: str, body: str = None) -> Response:
        res = await self._send(*args, body=body)
        res.raise_for_status()
        return res

    # === Commands

    async def _config_set_reset(self, cmd: str, args: typing.Iterable[str], kwargs: dict[str, typing.Any]):
        for name in args:
            if name in kwargs:
                raise ValueError(f'Cannot pass {name!r} as argument and keyword argument at same time')
            kwargs[name] = None

        res = []
        for name, value in kwargs.items():
            if not isinstance(value, list):
                value = [value]

            for val in value:
                if isinstance(val, bool):
                    val = int(val)

                if val is None:
                    line = name
                else:
                    line = name + '=' + qs(str(val))
                res.append(line)

        await self._sc(cmd, *res)

    async def config_set(self, name: str, value: typing.Any = None):
        await self._config_set_reset('SETCONF', (), {name: value})

    async def config_set_all(self, config: dict[str, typing.Any], reset: typing.Iterable[str] = ()):
        await self._config_set_reset('SETCONF', reset, config)

    async def config_reset(self, *names: str):
        await self._config_set_reset('RESETCONF', names, {})

    async def config_get(self, name: str):
        res = await self._sc('GETCONF', name)
        data, errors = res.data_to_paris('=', include_message=True)
        if len(data) == 1:
            return data[0][1]
        if not data:
            return None
        return [value for _, value in data]

    async def config_get_all(self, *keys: str):
        res = await self._sc('GETCONF', *keys)
        data, errors = res.data_to_paris('=', include_message=True)
        return data

    async def set_events(self, *codes: str, extended: bool = False):
        new_codes = []
        for code in codes:
            if isinstance(code, str):
                new_codes.append(code)
            else:
                keys = getattr(code, '__event_keys__', None)
                if keys:
                    new_codes.extend(keys)

        if extended:
            await self._sc('SETEVENTS', 'EXTENDED', *new_codes)
        else:
            await self._sc('SETEVENTS', *new_codes)

    async def authenticate_none(self):
        await self._sc('AUTHENTICATE')

    async def authenticate_password(self, password: str):
        await self._sc('AUTHENTICATE', qs(password))

    async def authenticate_cookie(self, data: bytes):
        await self._sc('AUTHENTICATE', data.hex())

    async def config_save(self, force: bool = False):
        if force:
            await self._sc('SAVECONF', 'FORCE')
        else:
            await self._sc('SAVECONF')

    async def signal(self, signal: TorSignal):
        await self._sc('SIGNAL', signal.value)

    async def map_address(self, old_address: str, new_address: str):
        mapped, errors = await self.map_addresses({old_address: new_address})
        if errors:
            raise errors[0]

    async def unmap_address(self, address: str):
        await self.map_address(address, '.')

    async def map_addresses(self, addr_tab: dict[str, str]) -> tuple[dict[str, str], list[TorException]]:
        res = await self._send('MAPADDRESS', *(f"{k}={v}" for k, v in addr_tab.items()))
        return res.data_to_dict('=', include_message=True)

    async def unmap_addresses(self, *addresses: str) -> tuple[list[str], list[TorException]]:
        res, err = await self.map_addresses({address: '.' for address in addresses})
        return list(res.keys()), err

    async def get_info(self, key: str) -> str:
        res = await self.get_infos(key)
        return res[key]

    async def get_infos(self, *keys: str) -> dict[str, str]:
        res = await self._sc('GETINFO', *keys)
        return res.data_to_dict('=')[0]

    async def extent_circuit(self, circuit_id: str, *specs: ServerSpec,
                             purpose: CircuitPurpose = CircuitPurpose.GENERAL):
        data = []
        for spec in specs:
            fp = spec.fingerprint
            if isinstance(fp, bytes):
                fp = fp.hex()

            if fp is not None and spec.nickname is not None:
                data.append(f'${fp}~{spec.nickname}')
            elif fp is not None:
                data.append(f'${fp}')
            elif spec.nickname is not None:
                data.append(spec.nickname)
            else:
                raise ValueError("Passed server spec has no fingerprint nor nickname")

        if purpose:
            data.append('purpose=' + purpose.value)

        res = await self._sc('EXTENDCIRCUIT', circuit_id, *data)
        _, _, circuit_id = res.message.partition(' ')
        return circuit_id

    async def set_circuit_purpose(self, circuit_id: str, purpose: CircuitPurpose):
        await self._sc('SETCIRCUITPURPOSE', circuit_id, 'purpose=' + purpose.value)

    async def set_router_purpose(self, nick_or_key, purpose: RouterPurpose):  # deprecated
        await self._sc('SETROUTERPURPOSE', nick_or_key, purpose.value)

    async def attach_stream(self, stream_id: str, circuit_id: str = '0', hop: int = -1):
        if hop < 1:
            await self._sc('ATTACHSTREAM', stream_id, circuit_id)
        else:
            await self._sc('ATTACHSTREAM', stream_id, circuit_id, 'HOP=' + str(hop))

    async def post_descriptor(self, descriptor: str, purpose: RouterPurpose = RouterPurpose.GENERAL,
                              cache: bool | None = None):
        data = []
        if purpose != RouterPurpose.GENERAL:
            data.append('purpose=' + purpose.value)

        if cache is not None:
            if cache:
                data.append('cache=yes')
            else:
                data.append('cache=no')

        await self._sc('POSTDESCRIPTOR', *data, body=descriptor)

    async def redirect_stream(self, stream_id: str, address: str, port: int = None):
        if port is None:
            await self._sc('REDIRECTSTREAM', stream_id, address)
        else:
            await self._sc('REDIRECTSTREAM', stream_id, address, str(port))

    async def close_stream(self, stream_id: str, reason: CloseStreamReason):
        await self._sc('CLOSESTREAM', stream_id, str(reason.value))

    async def close_circuit(self, circuit_id: str, if_unused: bool = False):
        flags = ('IfUnused',) if if_unused else ()
        await self._sc('CLOSECIRCUIT', circuit_id, *flags)

    async def quit(self):
        await self._sc('QUIT')

    async def use_features(self, *features: TorFeature):
        await self._sc('USEFEATURE', *(feature.value for feature in features))

    async def resolve(self, *addresses: str, reverse: bool = False):
        if reverse:
            addresses = ('mode=reverse',) + addresses
        await self._sc('RESOLVE', *addresses)

    async def get_protocol_info(self, *version):
        res = await self._sc('PROTOCOLINFO', *version)

        info = ProtocolInfo()
        for line in res.data:
            args, kwargs = line.parse_args_kwargs()
            if args[0] == 'PROTOCOLINFO':
                info.version = int(args[1])

            elif args[0] == 'VERSION':
                info.versions.update(kwargs)

            elif args[0] == 'AUTH':
                methods = kwargs.get('METHODS')
                if methods is not None:
                    info.auth_methods.extend((AuthMethod(method) for method in methods.split(',')))

                cookie_file = kwargs.get('COOKIEFILE')
                if cookie_file is not None:
                    info.cookie_file = cookie_file

            else:
                info.additional_info.append((args, kwargs))

        return info

    async def config_load(self, data: str):
        await self._sc('+LOADCONF\r\n' + data.replace('\n', '\r\n') + '\r\n.')

    async def take_ownership(self):
        await self._sc('TAKEOWNERSHIP')

    async def auth_challenge(self, client_nonce: str | bytes):
        if isinstance(client_nonce, str):
            client_nonce = qs(client_nonce)
        else:
            client_nonce = client_nonce.hex()

        res = await self._sc('AUTHCHALLENGE', 'SAFECOOKIE', client_nonce)
        _, res = res.data[0].parse_args_kwargs()

        server_hash = bytes.fromhex(res['SERVERHASH'])
        server_nonce = bytes.fromhex(res['SERVERNONCE'])
        return server_hash, server_nonce

    async def drop_guards(self):
        await self._sc('DROPGUARDS')

    async def hs_fetch_descid(self, desc_id: str, *servers: str):
        await self._sc('HSFETCH', 'v2-' + desc_id, *('SERVER=' + server for server in servers))

    async def hs_fetch(self, address: str, *servers: str):
        await self._sc('HSFETCH', address.removesuffix('.onion'), *('SERVER=' + server for server in servers))

    def add_onion_v2(self):
        return OnionBuilderV2(self)

    def add_onion(self):
        return OnionBuilderV3(self)

    async def del_onion(self, address: str):
        await self._sc('DEL_ONION', address.removesuffix('.onion'))

    async def hs_post(self, descriptor: str, address: str | None = None, *servers: str):
        args = []
        for server in servers:
            args.append('SERVER=' + server)
        if address:
            args.append('HSADDRESS=' + address.removesuffix('.onion'))
        await self._sc('HSPOST', *args, body=descriptor)

    async def client_auth_add(self, address: str, key: bytes, nickname: str = None, permanent = False):
        args = []
        if nickname is not None:
            args.append('ClientName=' + nickname)
        if permanent:
            args.append('Flags=Permanent')

        await self._sc('ONION_CLIENT_AUTH_ADD', address, 'x25519:' + base64.b64encode(key).decode(), *args)

    async def client_auth_remove(self, address: str):
        await self._sc('ONION_CLIENT_AUTH_REMOVE', address)

    async def client_auth_view(self, address: str = None) -> dict[str, tuple[bytes, str | None, bool]]:
        if address is None:
            res = await self._sc('ONION_CLIENT_AUTH_VIEW')
        else:
            res = await self._sc('ONION_CLIENT_AUTH_VIEW', address)

        data = {}
        for line in res.data:
            args, extra = line.parse_args_kwargs()
            if not args or args[0] != 'CLIENT':
                continue

            flags = extra.get('Flags')
            if flags:
                flags = flags.split(',')
            else:
                flags = ()

            key = base64.b64decode(args[2].removeprefix('x25519:'))
            data[args[1]] = (key, extra.get('ClientName'), 'Permanent' in flags)

        return data

    async def drop_ownership(self):
        await self._sc('DROPOWNERSHIP')

    async def drop_timeouts(self):
        await self._sc('DROPTIMEOUTS')

    # ==== High-level API

    async def auth(self, methods: typing.Iterable[AuthMethod] = DEFAULT_AUTH_METHODS, *, password: str = None):
        info = await self.get_protocol_info('1')
        for method in methods:
            if method not in info.auth_methods:
                continue

            if method == AuthMethod.NULL:
                await self.authenticate_none()
                return
            if password and method == AuthMethod.HASHED_PASSWORD:
                await self.authenticate_password(password)
                return
            if method == AuthMethod.COOKIE or method == AuthMethod.SAFE_COOKIE:
                try:
                    await self._do_auth_cookie(info.cookie_file, method == AuthMethod.SAFE_COOKIE)
                    return
                except OSError:
                    pass

        server = ', '.join((method.name for method in info.auth_methods))
        client = ', '.join((method.name for method in methods))
        raise ValueError(f'No supported auth methods found, server supports {server}, client wants {client}')

    async def _do_auth_cookie(self, path: str, safe: bool):
        with open(path, 'rb') as f:
            data = f.read()

        if safe:
            client_nonce = random.randbytes(32)
            server_hash, server_nonce = await self.auth_challenge(client_nonce)
            server_hash2 = hmac.HMAC(b"Tor safe cookie authentication server-to-controller hash",
                                    data + client_nonce + server_nonce, digestmod=hashlib.sha256).digest()
            if server_hash != server_hash2:
                raise TorProtocolException('Server hash mismatch')

            data = hmac.HMAC(b"Tor safe cookie authentication controller-to-server hash",
                            data + client_nonce + server_nonce, digestmod=hashlib.sha256).digest()

        await self.authenticate_cookie(data)


async def connect(host: str, port: int, *, loop=None, ssl=False, dispatcher: EventDispatcher | None = None):
    return AsyncConnection(await create_connection(host, port, loop=loop, ssl=ssl, dispatcher=dispatcher))


async def connect_unix(path: str, *, loop=None, ssl=False, dispatcher: EventDispatcher | None = None):
    return AsyncConnection(await create_unix_connection(path, loop=loop, ssl=ssl, dispatcher=dispatcher))
