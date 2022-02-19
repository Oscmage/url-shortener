from unittest import TestCase

from fastapi.testclient import TestClient

from app import main


class Test(TestCase):

    def setUp(self) -> None:
        self._client = TestClient(main.start())

    def test_get(self):
        response = self._client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'Hello': 'World'})

    def test_get_alias_not_found(self):
        response = self._client.get("/v1/bogus_alias")
        self.assertEqual(response.status_code, 404)

    def test_post_alias(self):
        alias = "XHIZJR"
        url = "http://oscar.com"
        response = self._client.post("/v1/url", json={"url": url, "alias": alias})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), dict(alias=alias, url=url))

    def test_post_alias_followed_by_get(self):
        alias = "XHIZJR"
        url = "http://oscar.com"
        post_response = self._client.post("/v1/url", json={"url": url, "alias": alias})
        self.assertEqual(post_response.status_code, 200)

        get_response = self._client.get(f"/v1/{alias}")
        self.assertEqual(get_response.status_code, 200)
