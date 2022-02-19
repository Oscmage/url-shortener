from typing import Optional

from url.alias_util import AliasUtil
from url.entry import UrlEntry
from url.exception import AliasAlreadyTakenError
from url.repository import UrlRepository


class UrlInterface:
    def __init__(self, repo: UrlRepository):
        self._repo = repo

    def get_url(self, alias: str) -> Optional[UrlEntry]:
        return self._repo.get_url(alias)

    def add_url(self, url: str, alias: Optional[str]) -> UrlEntry:
        if not alias:
            alias = AliasUtil.generate_alias()

        if self._repo.get_url(alias):
            raise AliasAlreadyTakenError()

        return self._repo.add_url(url, alias)
