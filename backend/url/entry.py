import dataclasses


@dataclasses.dataclass
class UrlEntry:
    id: int
    url: str
    alias: str

