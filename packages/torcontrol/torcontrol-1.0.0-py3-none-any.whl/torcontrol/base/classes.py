import dataclasses

from . import AuthMethod


@dataclasses.dataclass
class ServerSpec:
    fingerprint: str | bytes | None = None
    nickname: str | None = None


@dataclasses.dataclass
class ProtocolInfo:
    version: int = 1
    versions: dict[str, str] = dataclasses.field(default_factory=dict)
    auth_methods: list[AuthMethod] = dataclasses.field(default_factory=list)
    cookie_file: str | None = None
    additional_info: list = dataclasses.field(default_factory=list)
