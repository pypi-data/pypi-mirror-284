import base64
import typing


class _OnionBuilder:
    version: int

    def __init__(self, conn):
        self._conn = conn

        self._max_streams = 0
        self._max_streams_close_circuit = False
        self._ports = []
        self._non_anonymous = False
        self._key = None
        self._discard_pk = False
        self._detach = False
        self._auth = None

    def set_max_streams(self, count: int = 0, *, close_circuit: bool = False) -> typing.Self:
        self._max_streams = count
        self._max_streams_close_circuit = close_circuit
        return self

    def add_port(self, port: int, target: tuple[str, int] | int | None = None) -> typing.Self:
        if isinstance(target, int):
            target = str(target)
        elif target is not None:
            target = target[0] + ':' + str(target[1])
        self._ports.append((port, target))
        return self

    def set_non_anonymous(self, value: bool) -> typing.Self:
        self._non_anonymous = value
        return self

    def use_key(self, key_data: str | bytes) -> typing.Self:
        if isinstance(key_data, bytes):
            key_data = base64.b64encode(key_data).decode()

        self._key = key_data
        self._discard_pk = False
        return self

    def use_new_key(self, *, discard_pk: bool = False) -> typing.Self:
        self._key = None
        self._discard_pk = discard_pk
        return self

    def set_detach(self, value: bool) -> typing.Self:
        self._detach = value
        return self

    async def build(self):
        res = ['ADD_ONION']

        if self._key is None:
            if self.version == 2:
                res.append('NEW:RSA1024')
            elif self.version == 3:
                res.append('NEW:ED25519-V3')
            else:
                raise ValueError(f'Invalid version: {self.version}')
        else:
            if self.version == 2:
                res.append('RSA1024:' + self._key)
            elif self.version == 3:
                res.append('ED25519-V3:' + self._key)
            else:
                raise ValueError(f'Invalid version: {self.version}')

        flags = []
        if self._discard_pk:
            flags.append('DiscardPK')
        if self._detach:
            flags.append('Detach')
        if self._auth is not None:
            if self.version == 2:
                flags.append('BasicAuth')
            else:
                flags.append('V3Auth')
        if self._non_anonymous:
            flags.append('NonAnonymous')
        if self._max_streams_close_circuit:
            flags.append('MaxStreamsCloseCircuit')

        if flags:
            res.append('Flags=' + ','.join(flags))

        if self._max_streams != 0:
            res.append('MaxStreams=' + str(self._max_streams))

        for port, target in self._ports:
            port = str(port)
            if target is not None:
                port += ',' + str(target)
            res.append('Port=' + port)

        if self.version == 2 and self._auth is not None:
            for name, blob in self._auth:
                if blob is not None:
                    name += ':' + blob  # TODO
                res.append('ClientAuth=' + name)
        if self.version == 3 and self._auth is not None:
            res.append('ClientAuthV3=' + self._auth)

        res = await self._conn._sc(*res)
        res, _ = res.data_to_paris('=')
        keys = []
        pk = None
        sid = None
        for key, value in res:
            if key == 'ServiceID':
                sid = value
            elif key == 'PrivateKey':
                _, _, pk = value.partition(':')
                pk = base64.b64decode(pk)
            elif key == 'ClientAuth':
                keys.append(value)

        return pk, sid, keys


class OnionBuilderV2(_OnionBuilder):
    version = 2

    def auth_add_client(self, name: str, blob: bytes | None = None) -> typing.Self:
        if self._auth is None:
            self._auth = []
        self._auth.append((name, blob))
        return self


class OnionBuilderV3(_OnionBuilder):
    version = 3

    def set_auth_cert(self, cert) -> typing.Self:
        self._auth = cert
        return self
