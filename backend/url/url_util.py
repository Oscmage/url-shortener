import validators

from url.exception import InvalidUrlError


class UrlUtil:

    @staticmethod
    def validate_url(url: str) -> None:
        try:
            validators.url(url)
        except validators.ValidationFailure:
            raise InvalidUrlError("Invalid URL")
