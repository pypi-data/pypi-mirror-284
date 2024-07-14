import dataclasses
import typing


LOG_EVENTS = {"DEBUG", "INFO", "NOTICE", "WARN", "ERR"}
_EVENT_TYPES = {}


class _Field(typing.NamedTuple):
    arg: str | int | None
    map: dict[str, typing.Any] | typing.Callable[[str], typing.Any] | None
    default: typing.Any
    field_name: str | None = None


class EventMeta(type):
    def __new__(mcs, name, bases, attrs, **kwargs):
        if name == 'Event':
            return type.__new__(mcs, name, bases, attrs)

        event_keys = kwargs.get("events", ())
        event_key = kwargs.get("event")
        if event_key is not None:
            event_keys = event_keys + (event_key,)

        c_data = []
        for name, value in list(attrs.items()):
            if not isinstance(value, _Field):
                continue

            del attrs[name]
            value = _Field(*value[:-1], name)
            c_data.append(value)

        attrs['__construct_data__'] = tuple(c_data)
        attrs['__event_keys__'] = frozenset(event_keys)
        cls = type.__new__(mcs, name, bases, attrs)
        cls = dataclasses.dataclass(frozen=True)(cls)

        for event_key in event_keys:
            _EVENT_TYPES[event_key] = cls

        return cls


def field(arg: int | str | None = None, *,
          map: dict[str, typing.Any] | typing.Callable[[str], typing.Any] | None = None,
          default: typing.Any = None) -> _Field:
    return _Field(arg, map, default)


def flag_field(arg: int | str | None, flag_name: str):
    return field(arg, default=False, map=lambda s: flag_name in s.split(','))


class Event(metaclass=EventMeta):
    @classmethod
    def construct(cls, args, kwargs, data):
        res = {}
        c_data: tuple[_Field, ...] = getattr(cls, '__construct_data__', ())

        for field in c_data:
            if isinstance(field.arg, int):
                if field.arg >= len(args):
                    value = field.default
                else:
                    value = args[field.arg]

            elif isinstance(field.arg, str):
                value = kwargs.get(field.arg, field.default)
            else:
                value = data

            if isinstance(field.map, dict):
                value = field.map.get(value, field.default)
            elif callable(field.map) and value is not None:
                value = field.map(value)

            res[field.field_name] = value

        return cls(**res)


def _construct_event(key: str, args: tuple[str, ...], kwargs: dict[str, str], data: list[str]) -> Event:
    event_cls = _EVENT_TYPES.get(key)
    if event_cls is None:
        raise ValueError("Unsupported event type")

    return event_cls.construct(args, kwargs, data)


class EventDispatcher:
    __slots__ = ("_handlers",)

    def __init__(self):
        self._handlers: dict[str, typing.Callable[[Event], ...]] = {}

    def add_handler(self, events: typing.Iterable[str | type[Event]], handler: typing.Callable[[Event], ...]):
        for events2 in events:
            if isinstance(events2, str):
                events2 = (events2, )
            else:
                events2 = getattr(events2, '__event_keys__', ())

            for event in events2:
                self._handlers[event] = handler

    def handler(self, *events: str | type[Event]):
        def _wrapper(handler: typing.Callable[[Event], ...]):
            self.add_handler(events, handler)
            return handler
        return _wrapper

    def dispatch(self, message: 'Response'):
        if not message.is_async_event():
            raise ValueError("Message is not an event")

        key, _, text = message.data[0].data.partition(' ')

        if key in LOG_EVENTS:  # Special case: log events format is SEVERITY MESSAGE... or SEVERITY\nMESSAGE\nOK
            if len(message.data) > 1:
                text = '\n'.join((line.data for line in message.data[1:-1]))

            args = (key, text, )
            key = 'LOG'
            kwargs = {}
            data = []
        else:
            args, kwargs = message.data[0].parse_args_kwargs()
            args = args[1:]
            data = [line.data for line in message.data[1:]]

        handler = self._handlers.get(key)
        if handler is None:
            return

        event = _construct_event(key, args, kwargs, data)
        handler(event)
