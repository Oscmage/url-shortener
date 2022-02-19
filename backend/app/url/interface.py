from typing import Optional

from app.url.alias_util import AliasUtil
from app.url.entry import UrlEntry
from app.exception import AliasAlreadyTakenError
from app.url.repository import UrlRepository


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
