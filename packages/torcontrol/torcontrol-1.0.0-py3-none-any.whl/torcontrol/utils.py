import asyncio
import queue


def unqoute(key: str):
    if key and key[0] == '"' and key[-1] == '"':
        return key[1:-1].replace('\\"', '"').replace('\\\\', '\\')
    return key


def qs(s: str) -> str:
    return '"' + s.replace('"', '\\"') + '"'  # TODO


async def aio_queue_get(q: asyncio.Queue, timeout: float | None = None):
    if timeout is not None and timeout < 0:
        try:
            return q.get_nowait()
        except asyncio.QueueEmpty:
            raise TimeoutError()

    async with asyncio.timeout(timeout):
        return await q.get()


def queue_get(q: queue.Queue, timeout: float | None = None):
    if timeout is not None and timeout < 0:
        try:
            return q.get_nowait()
        except queue.Empty:
            raise TimeoutError()

    try:
        return q.get(timeout=timeout)
    except queue.Empty:
        raise TimeoutError()


def split(s: str, k: str) -> list[str]:
    if not s:
        return []
    return s.split(k)
