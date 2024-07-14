import typing


def encode_request(request: typing.Iterable[str], body: str | None = None) -> str:
    request = ' '.join(request) + '\r\n'
    if body is not None:
        request = '+' + request + body.replace('\n', '\r\n') + '\r\n.\r\n'
    return request


def encode_request_b(request: typing.Iterable[str], body: str | None = None) -> bytes:
    return encode_request(request, body).encode('utf-8')
