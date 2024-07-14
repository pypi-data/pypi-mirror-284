import asyncio
import queue

from torcontrol.base import TorStatus
from torcontrol.errors import TorProtocolException, ConnectionClosedException
from . import ResponseLine, Response
from ..events import EventDispatcher
from ..utils import aio_queue_get


class ResponseDecoder:
    def __init__(self):
        self._saved_end = b''
        self._multiline_code = None
        self._multiline_data = []
        self._lines = []

    def feed_line(self, line: str):
        if self._multiline_code is None:
            if not line:
                return

            if len(line) < 5 or not line[:3].isdigit():
                raise TorProtocolException(f"Got malformed line: {line!r}")

            code = TorStatus(int(line[:3]))
            spec = line[3]
            line = line[4:]

            # 250+SOME TEXT => SET ML
            if spec == '+':
                self._multiline_code = code
                self._multiline_data = [line]

            # 250-SOME TEXT => APPEND
            elif spec in '-':
                self._lines.append(ResponseLine(code, line))

            # 250 SOME TEXT => EOM
            elif spec == ' ':
                self._lines.append(ResponseLine(code, line))
                self.on_message(Response(self._lines))
                self._lines = []

            else:
                raise TorProtocolException(f"Got malformed line: {line!r}")

        else:
            if line == '.':
                line = '\n'.join(self._multiline_data)
                self._lines.append(ResponseLine(self._multiline_code, line))
                self._multiline_data.clear()
                self._multiline_code = None
            else:
                self._multiline_data.append(line)

    def feed_line_b(self, data: bytes):
        self.feed_line(data.decode('utf-8'))

    def feed(self, data: str):
        data = data.split('\r\n')
        for line in data:
            self.feed_line(line)

    def feed_b(self, data: bytes):
        save_end = not data.endswith(b'\r\n')
        data = self._saved_end + data
        data = data.split(b'\r\n')
        self._saved_end = data.pop(-1) if save_end else b''

        for line in data:
            self.feed_line_b(line)

    def close(self):
        if self._saved_end:
            raise TorProtocolException("Unexpected EOF")

    def on_message(self, message: Response):
        raise NotImplementedError()


class ListResponseDecoder(ResponseDecoder):
    def __init__(self):
        super().__init__()
        self.messages: list[Response] = []

    def on_message(self, message: Response):
        self.messages.append(message)


class EventsResponseDecoder(ResponseDecoder):
    def __init__(self, dispatcher: EventDispatcher | None = None):
        super().__init__()
        self._dispatcher = dispatcher

    def on_message(self, message: Response):
        if self._dispatcher is not None and message.is_async_event():
            self._dispatcher.dispatch(message)


class QueueResponseDecoder(ResponseDecoder):
    def __init__(self, q, dispatcher: EventDispatcher | None = None):
        super().__init__()
        self._queue = q
        self._dispatcher = dispatcher

    def on_message(self, message: Response):
        if not message.is_async_event():
            self._queue.put_nowait(message)
        elif self._dispatcher is not None:
            self._dispatcher.dispatch(message)

    def close(self):
        super().close()
        self._queue.put_nowait(None)


class AsyncQueueResponseDecoder(QueueResponseDecoder):
    def __init__(self, q: asyncio.Queue | None = None, dispatcher: EventDispatcher | None = None):
        if q is None:
            q = asyncio.Queue()
        super().__init__(q, dispatcher)

    async def get(self, timeout=None):
        res = await aio_queue_get(self._queue, timeout)
        if res is None:
            raise ConnectionClosedException()
        return res


class SyncQueueResponseDecoder(QueueResponseDecoder):
    def __init__(self, q: queue.Queue | None = None, dispatcher: EventDispatcher | None = None):
        if q is None:
            q = queue.Queue()
        super().__init__(q, dispatcher)

    def get(self, timeout=None):
        res = aio_queue_get(self._queue, timeout)
        if res is None:
            raise ConnectionClosedException()
        return res
