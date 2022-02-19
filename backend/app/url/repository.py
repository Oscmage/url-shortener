from typing import Dict, Optional

from app.url.entry import UrlEntry


class UrlRepository:

    def __init__(self):
        self._id = 0
        self._db: Dict[str, UrlEntry] = {}

    def get_url(self, alias: str) -> Optional[UrlEntry]:
        return self._db.get(alias)

    def add_url(self, url: str, alias: str) -> UrlEntry:
        entry = UrlEntry(
            id=self._id,
            url=url,
            alias=alias,
        )
        assert alias not in self._db, "Alias already in db"
        self._db[alias] = entry
        self._id += 1
        return entry
