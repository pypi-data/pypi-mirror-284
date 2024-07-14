import datetime

from torcontrol.events import Event, field, flag_field
from torcontrol.utils import split


class CircuitEvent(Event, event="CIRC"):
    id: str  = field(0)
    status: str = field(1)  # LAUNCHED, BUILT, GUARD_WAIT, EXTENDED, FAILED, CLOSED
    path: list[str] = field(2, default='', map=lambda s: split(s, ','))

    onehop_tunnel: bool = flag_field('BUILD_FLAGS', 'ONEHOP_TUNNEL')
    is_internal: bool = flag_field('BUILD_FLAGS', 'IS_INTERNAL')
    need_capacity: bool = flag_field('BUILD_FLAGS', 'NEED_CAPACITY')
    need_uptime: bool = flag_field('BUILD_FLAGS', 'NEED_UPTIME')

    purpose: str | None = field('PURPOSE')  # GENERAL, HS_CLIENT_INTRO, HS_CLIENT_REND, HS_SERVICE_INTRO, HS_SERVICE_REND, TESTING,
    # CONTROLLER, MEASURE_TIMEOUT, HS_VANGUARDS, PATH_BIAS_TESTING, CIRCUIT_PADDING
    hs_state: str | None = field('HS_STATE')  # HSCI_CONNECTING, HSCI_INTRO_SENT, HSCI_DONE, HSCR_CONNECTING, HSCR_ESTABLISHED_IDLE,
    # HSCR_ESTABLISHED_WAITING, HSCR_JOINED, HSSI_CONNECTING, HSSI_ESTABLISHED, HSSR_CONNECTING, HSSR_JOINED
    rend_query: str | None = field('REND_QUERY')  # 16*Base32Character / 56*Base32Character
    time_created: datetime.datetime | None = field('TIME_CREATED', map=lambda x: datetime.datetime.fromisoformat(x))
    reason: str | None = field('REASON')  # NONE, TORPROTOCOL, INTERNAL, REQUESTED, HIBERNATING, RESOURCELIMIT, CONNECTFAILED,
    # OR_IDENTITY, OR_CONN_CLOSED, TIMEOUT, FINISHED, DESTROYED, NOPATH, NOSUCHSERVICE, MEASUREMENT_EXPIRED
    remote_reason: str | None = field('REMOTE_REASON')  # ^same

    socks_username: str | None = field('SOCKS_USERNAME')
    socks_password: str | None = field('SOCKS_PASSWORD')
    hs_pow: int | None = field('HS_POW', map=lambda s: int(s.removeprefix('v1,')))


class StreamEvent(Event, event="STREAM"):
    id: str = field(0)
    status: str = field(1)  # NEW, NEWRESOLVE, REMAP, SENTCONNECT, SENTRESOLVE, SUCCEEDED, FAILED, CLOSED, DETACHED
    circuit_id: str = field(2)
    target: str = field(3)  # address:port

    reason: str | None = field('REASON')  # MISC, RESOLVEFAILED, CONNECTREFUSED, EXITPOLICY, DESTROY, DONE, TIMEOUT,
    # NOROUTE, HIBERNATING, INTERNAL, RESOURCELIMIT, CONNRESET, TORPROTOCOL, NOTDIRECTORY, END, PRIVATE_ADDR
    remote_reason: str | None = field('REMOTE_REASON')  # ^same

    source: str | None = field('SOURCE')  # CACHE, EXIT
    source_address: str | None = field('SOURCE_ADDRESS')  # address:port
    purpose: str | None = field('PURPOSE')  # DIR_FETCH, DIR_UPLOAD, DNS_REQUEST, USER, DIRPORT_TEST

    socks_username: str | None = field('SOCKS_USERNAME')
    socks_password: str | None = field('SOCKS_PASSWORD')

    client_protocol: str | None = field('CLIENT_PROTOCOL')
    nym_epoch: str | None = field('NYM_EPOCH')
    session_group: str | None = field('SESSION_GROUP')
    iso_fields: list[str] | None = field('ISO_FIELDS', map=lambda s: split(s, ','))


class OrConnectionEvent(Event, event="ORCONN"):
    target: str = field(0)
    status: str = field(1)  # NEW, LAUNCHED, CONNECTED, FAILED, CLOSED

    reason: str | None = field('REASON')  # MISC, DONE, CONNECTREFUSED, IDENTITY, CONNECTRESET, TIMEOUT, NOROUTE,
    # IOERROR, RESOURCELIMIT, PT_MISSING
    ncircuits: int | None = field('NCIRCS', map=int)
    conn_id: str | None = field('CONN_ID')


class BandwidthEvent(Event, event="BW"):
    bytes_read: int = field(0, map=int)
    bytes_written: int = field(1, map=int)

    # additional_info = field(..., map=int)  # TODO


class LogEvent(Event, event="LOG"):
    severity: str = field(0)
    text: str = field(1)


class NewDescriptorEvent(Event, event="NEWDESC"):
    descriptor: str = field(0)  # TODO may be more than one


class NewAddressMappingEvent(Event, event="ADDRMAP"):
    address: str = field(0)
    new_address: str = field(1)
    expiry: str = field(2)  # iso time | "NEVER", deprecated

    error_code: str = field("error")
    expires: datetime.datetime | None = field("EXPIRES", map=lambda x: datetime.datetime.fromisoformat(x))
    cached: bool = field("CACHED", map=dict(YES=True, NO=False))


# AUTHDIR_NEWDESCS


class DescriptorChangedEvent(Event, event="DESCCHANGED"):
    pass


# 'STATUS_GENERAL', 'STATUS_CLIENT', 'STATUS_SERVER',
class StatusEvent(Event, event="STATUS"):
    pass  # TODO

class GuardEvent(Event, event="GUARD"):
    name: str = field(1)
    status: str = field(2)  # "NEW" | "UP" | "DOWN" | "BAD" | "GOOD" | "DROPPED"


class NetworkStatusEvent(Event, event="NS"):
    data = field()


class NetworkLivenessEvent(Event, event="NETWORK_LIVENESS"):
    connected: bool  = field(0, map=dict(UP=True, DOWN=False))


class StreamBandwidthEvent(Event, event="STREAM_BW"):
    stream_id: str = field(0)
    bytes_written: int = field(1, map=int)
    bytes_read: int = field(2, map=int)
    time: datetime.datetime = field(3, map=lambda x: datetime.datetime.fromisoformat(x))


class ClientsSeenEvent(Event, event="CLIENTS_SEEN"):
    time_started: datetime.datetime = field("TimeStarted", map=lambda x: datetime.datetime.fromisoformat(x))
    country_summary: dict[str, int] = field("CountrySummary", map=lambda s: dict((i.split('=') for i in s.split(','))))  # TODO convert to int
    ip_versions: dict[str, int] = field("IPVersions", map=...)  # ^same


class NewConsensusEvent(Event, event="NEWCONSUS"):
    data = field()


class BuildTimeoutSetEvent(Event, event="BUILDTIMEOUT_SET"):
    type: str = field(0)  #


# 'SIGNAL',
# 'CONF_CHANGED',
# 'CIRC_MINOR',
# 'TRANSPORT_LAUNCHED',
# 'CONN_BW',
# 'CIRC_BW',
# 'CELL_STATS',
# 'HS_DESC',
# 'HS_DESC_CONTENT',  ML

# -- PT_STATUS PT_LOG
