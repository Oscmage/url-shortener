import validators

from exception import InvalidUrlError


class UrlUtil:

    @staticmethod
    def validate_url(url: str) -> None:
        success = validators.url(url)
        if isinstance(success, bool) and success:
            return None

        raise InvalidUrlError("Invalid URL")