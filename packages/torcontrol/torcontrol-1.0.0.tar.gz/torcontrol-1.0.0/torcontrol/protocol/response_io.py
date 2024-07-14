from . import Response, ListResponseDecoder


def encode_response(message: Response) -> str:
    res = []
    for line in message.data[:-1]:
        if '\n' in line.data:
            lines = line.data.split('\n')
            res.append(f'{line.status}+{lines[0]}')
            res.extend(lines[1:])
            res.append('.')
        else:
            res.append(f'{line.status}-{line.data}')

    res.append(f'{message.status} {message.message}')
    return '\r\n'.join(res)


def encode_response_b(message: Response) -> bytes:
    return encode_response(message).encode('utf-8')


def decode_response(data: str) -> list[Response]:
    decoder = ListResponseDecoder()
    decoder.feed(data)
    return decoder.messages


def decode_response_b(data: bytes) -> list[Response]:
    decoder = ListResponseDecoder()
    decoder.feed_b(data)
    return decoder.messages
