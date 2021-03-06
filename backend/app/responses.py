import dataclasses
from typing import Optional

from app.url.entry import UrlEntry


@dataclasses.dataclass
class GetAliasRequest:
    alias: str


@dataclasses.dataclass
class PostAliasRequest:
    url: str
    alias: Optional[str] = None


@dataclasses.dataclass
class PostAliasResponse:
    url: str
    alias: str

    @classmethod
    def from_url_entry(cls, url_entry: UrlEntry):
        return cls(
            url=url_entry.url,
            alias=url_entry.alias
        )