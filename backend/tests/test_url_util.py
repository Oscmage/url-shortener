from unittest import TestCase

from exception import InvalidUrlError
from url.url_util import UrlUtil


class TestUrlUtil(TestCase):

    def test_validate_url_success(self):
        http_url = "http://oscar.com"
        UrlUtil.validate_url(http_url)

        https_url = "https://oscar.com"
        UrlUtil.validate_url(https_url)

    def test_validate_url_raises(self):
        invalid_url = "httpqweqwe://oscar.com"
        self.assertRaises(InvalidUrlError, UrlUtil.validate_url, invalid_url)
