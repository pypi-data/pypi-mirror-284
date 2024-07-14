import enum


class TorSignal(enum.Enum):
    RELOAD = "RELOAD"
    SHUTDOWN = "SHUTDOWN"
    DUMP = "DUMP"
    DEBUG = "DEBUG"
    HALT = "HALT"
    CLEAR_DNS_CACHE = "CLEARDNSCACHE"
    NEW_NYM = "NEWNYM"
    HEARTBEAT = "HEARTBEAT"
    DORMANT = "DORMANT"
    ACTIVE = "ACTIVE"


class CircuitPurpose(enum.Enum):
    GENERAL = "general"
    CONTROLLER = "controller"


class RouterPurpose(enum.Enum):
    GENERAL = "general"
    CONTROLLER = "controller"
    BRIDGE = "bridge"


class CloseStreamReason(enum.IntEnum):
    MISC = 1
    RESOLVEFAILED = 2
    CONNECTREFUSED = 3
    EXITPOLICY = 4
    DESTROY = 5
    DONE = 6
    TIMEOUT = 7
    NOROUTE = 8
    HIBERNATING = 9
    INTERNAL = 10
    RESOURCELIMIT = 11
    CONNRESET = 12
    TORPROTOCOL = 13
    NOTDIRECTORY = 14


class TorFeature(enum.Enum):
    EXTENDED_EVENTS = "EXTENDED_EVENTS"
    VERBOSE_NAMES = "VERBOSE_NAMES"


class TorStatus(enum.IntEnum):
    OK = 250
    UNNECESSARY = 251

    RESOURCE_EXHAUSTED = 451

    SYNTAX_ERROR_PROTOCOL = 500
    UNRECOGNIZED_COMMAND = 510
    UNIMPLEMENTED_COMMAND = 511
    SYNTAX_ERROR_ARGUMENT = 512
    UNRECOGNIZED_ARGUMENT = 513
    AUTHENTICATION_REQUIRED = 514
    BAD_AUTHENTICATION = 515
    UNSPECIFIED_TOR_ERROR = 550
    INTERNAL_ERROR = 551
    UNRECOGNIZED_ENTITY = 552
    INVALID_CONFIG_VALUE = 553
    INVALID_DESCRIPTOR = 554
    UNMANAGED_ENTITY = 555

    ASYNC_EVENT = 650

    def is_success(self):
        return 200 <= self.value < 299 or self.is_async_event()

    def is_async_event(self):
        return 600 <= self.value <= 699


class AuthMethod(enum.Enum):
    NULL = 'NULL'
    HASHED_PASSWORD = 'HASHEDPASSWORD'
    COOKIE = 'COOKIE'
    SAFE_COOKIE = 'SAFECOOKIE'
