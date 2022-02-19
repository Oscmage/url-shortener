import random
import string

from app.exception import InvalidAliasLengthError, InvalidAliasError


class AliasUtil:
    SHORT_ALIAS_LENGTH = 6
    VALID_CHARACTERS_LIST = string.ascii_letters + string.digits + "-" + "_"
    VALID_CHARACTERS_SET = set(VALID_CHARACTERS_LIST)

    @staticmethod
    def generate_alias(length: int = SHORT_ALIAS_LENGTH) -> str:
        return ''.join(random.SystemRandom().choice(AliasUtil.VALID_CHARACTERS_LIST) for _ in range(length))

    @staticmethod
    def validate_alias(url: str, alias: str) -> None:
        if len(alias) > len(url):
            raise InvalidAliasLengthError("Url longer than alias")

        for c in alias:
            if c not in AliasUtil.VALID_CHARACTERS_SET:
                raise InvalidAliasError(
                    f"{c} is not a valid character, only alphanumeric symbols, dash or underscore are allowed"
                )
