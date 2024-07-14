import typing

from torcontrol.base import TorStatus
from torcontrol.errors import TorException, TorProtocolException
from torcontrol.utils import unqoute


class ResponseLine(typing.NamedTuple):
    status: TorStatus
    data: str

    def parse_args_kwargs(self) -> tuple[tuple[str, ...], dict[str, str]]:
        if not self.data:
            return (), {}

        args = []
        kwargs = {}
        parsing_kwargs = False
        for arg in self.data.split(' '):
            key, eq, value = arg.partition('=')
            if eq:
                parsing_kwargs = True
                kwargs[key] = unqoute(value)
            else:
                if parsing_kwargs:
                    raise TorProtocolException("Argument after keyword arguments: " + self.data)
                args.append(arg)

        return tuple(args), kwargs


class Response:
    __slots__ = ('data', )

    def __init__(self, data: list[ResponseLine]):
        self.data = data

    @classmethod
    def single_line(cls, code: TorStatus, data: str) -> 'Response':
        return cls([ResponseLine(code, data)])

    @property
    def status(self) -> TorStatus:
        return self.data[-1].status

    @property
    def message(self) -> str:
        return self.data[-1].data

    def is_async_event(self):
        return self.status.is_async_event()

    def raise_for_status(self):
        if not self.status.is_success():
            raise TorException(self.status, self.message)

    def data_to_paris(self, sep: str, *, include_first_line=True, include_message=False, only_with_value=False)\
            -> tuple[list[tuple[str, str | None]], list[TorException]]:
        messages = self.data if include_message else self.data[:-1]
        messages = messages if include_first_line else messages[1:]

        res = []
        errors = []
        for line in messages:
            if line.status.is_success():
                key, s, value = line.data.partition(sep)
                if s or not only_with_value:
                    res.append((key, value if s else None))
            else:
                errors.append(TorException(line.status, line.data))

        return res, errors

    def data_to_dict(self, sep: str, **kwargs) -> tuple[dict[str, str | None], list[TorException]]:
        res, errors = self.data_to_paris(sep, **kwargs)
        return dict(res), errors
