import asyncio

from torcontrol.errors import ConnectionClosedException
from torcontrol.events import EventDispatcher
from torcontrol.protocol import encode_request_b, Response, AsyncQueueResponseDecoder


class ControlProtocol(asyncio.Protocol):
    def __init__(self, dispatcher: EventDispatcher | None = None):
        self._transport: asyncio.Transport | None = None
        self._decoder = AsyncQueueResponseDecoder(dispatcher=dispatcher)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self._transport is not None:
            self._transport.close()

    @property
    def is_closed(self):
        return self._transport is None or self._transport.is_closing()

    async def request(self, *data: str, body: str | None = None, timeout: float | None = None) -> Response:
        self.write(*data, body=body)
        return await self.get(timeout)

    def write(self, *data: str, body: str | None = None):
        data = encode_request_b(data, body)

        if self.is_closed:
            raise ConnectionClosedException()

        self._transport.write(data)

    async def get(self, timeout=None):
        if self.is_closed:
            raise ConnectionClosedException()
        return await self._decoder.get(timeout)

    # ==== internal

    def connection_made(self, transport):
        self._transport = transport

    def connection_lost(self, exc):
        self._transport = None
        self._decoder.close()

    def data_received(self, data: bytes):
        if self._transport is not None:
            self._decoder.feed_b(data)

    def eof_received(self):
        self.close()


async def create_connection(host: str, port: int, *, loop=None, ssl=False, dispatcher: EventDispatcher | None = None):
    if loop is None:
        loop = asyncio.get_running_loop()

    transport, protocol = await loop.create_connection(lambda: ControlProtocol(dispatcher), host, port, ssl=ssl)
    return protocol


async def create_unix_connection(path: str, *, loop=None, ssl=False, dispatcher: EventDispatcher | None = None):
    if loop is None:
        loop = asyncio.get_running_loop()

    transport, protocol = await loop.create_unix_connection(lambda: ControlProtocol(dispatcher), path, ssl=ssl)
    return protocol
