import validators

from app.exception import InvalidUrlError


class UrlUtil:

    @staticmethod
    def validate_url(url: str) -> None:
        success = validators.url(url)
        print(f"{success=}")
        if isinstance(success, bool) and success:
            return None

        raise InvalidUrlError("Invalid URL")