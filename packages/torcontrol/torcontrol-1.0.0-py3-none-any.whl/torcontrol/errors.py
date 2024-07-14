

class TorProtocolException(Exception):
    pass


class TorException(Exception):
    def __init__(self, code: int, message: str):
        super().__init__(f'{code} {message}')
        self.code = code
        self.message = message

    def __repr__(self):
        return f'<{type(self).__name__} {self.code} {self.message}>'


class ConnectionClosedException(Exception):
    pass
