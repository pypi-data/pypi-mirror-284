import socket

from torcontrol.errors import ConnectionClosedException
from torcontrol.events import EventDispatcher
from torcontrol.protocol import SyncQueueResponseDecoder, Response, encode_request_b


class ControlSocket:
    def __init__(self, sock: socket.socket, dispatcher: EventDispatcher | None = None):
        self._sock = sock
        self._decoder = SyncQueueResponseDecoder(dispatcher=dispatcher)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self._sock.close()

    @property
    def is_closed(self):
        return self._sock  # TODO

    def request(self, *data: str, body: str | None = None, timeout: float | None = None) -> Response:
        self.write(*data, body=body)
        return self.get(timeout)

    def write(self, *data: str, body: str | None = None):
        data = encode_request_b(data, body)

        if self.is_closed:
            raise ConnectionClosedException()

        self._sock.send(data)

    def get(self, timeout=None):
        if self.is_closed:
            raise ConnectionClosedException()
        return self._decoder.get(timeout)

    def start(self):
        while True:
            buf = self._sock.recv(1024)
            self._decoder.feed_b(buf)
