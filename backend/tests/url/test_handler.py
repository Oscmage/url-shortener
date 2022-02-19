from unittest import TestCase

from app import exception
from app.url.interface import UrlInterface
from app.url.repository import UrlRepository
from app.url.handler import UrlHandler
from app.url.alias_util import AliasUtil


class TestUrlHandler(TestCase):

    def setUp(self) -> None:
        url_repo = UrlRepository()
        url_interface = UrlInterface(
            url_repo
        )
        self._handler = UrlHandler(
            url_interface
        )
        self._valid_url = "https://oscar.com"

    def test_add_url_invalid_url(self):
        self.assertRaises(exception.InvalidUrlError, self._handler.add_url, url="invalid_url")

    def test_add_url_invalid_alias_length(self):
        self.assertRaises(exception.InvalidAliasLengthError, self._handler.add_url, url=self._valid_url,
                          alias="a_alias_longer_than_the_url")

    def test_add_url_invalid_alias_characters(self):
        self.assertRaises(exception.InvalidAliasError, self._handler.add_url, url="https://oscar.com", alias="!")

    def test_add_url_same_alias_raises(self):
        alias = "ABCD"
        self._handler.add_url(url=self._valid_url, alias=alias)

        self.assertRaises(exception.AliasAlreadyTakenError, self._handler.add_url, url=self._valid_url, alias=alias)

    def test_add_url_generates_alias(self):
        res = self._handler.add_url(url=self._valid_url)

        self.assertIsNotNone(res.alias)
        AliasUtil.validate_alias(url=res.url, alias=res.alias)

    def test_get_url(self):
        # Given
        add_res = self._handler.add_url(url=self._valid_url)

        # When
        res = self._handler.get_url(add_res.alias)

        # Then
        self.assertIsNotNone(res)
