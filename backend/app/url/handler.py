from typing import Optional

from app.url.alias_util import AliasUtil
from app.url.entry import UrlEntry
from app.url.interface import UrlInterface
from app.url.url_util import UrlUtil


class UrlHandler:

    def __init__(self, interface: UrlInterface) -> None:
        self._interface = interface

    def get_url(self, alias: str) -> Optional[UrlEntry]:
        return self._interface.get_url(alias)

    def add_url(self, url: str, alias: Optional[str] = None) -> UrlEntry:
        url = url.strip()
        UrlUtil.validate_url(url)
        if alias:
            alias = alias.strip()
            AliasUtil.validate_alias(url=url, alias=alias)

        return self._interface.add_url(url, alias)
