from fastapi import FastAPI

import error_codes
from url.exception import InvalidUrlError, InvalidAliasLengthError, InvalidAliasError, AliasAlreadyTakenError
from url.handler import UrlHandler
from url.handler_dto import PostAliasRequest, GetAliasResponse
from url.interface import UrlInterface
from url.repository import UrlRepository


def start():
    app = FastAPI()
    url_repo = UrlRepository()
    url_interface = UrlInterface(
        url_repo
    )
    url_handler = UrlHandler(
        url_interface
    )

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.get("/v1/{alias}")
    def get_alias(alias: str):
        if not alias:
            raise error_codes.NO_ALIAS_PROVIDED

        url_entry = url_handler.get_url(alias)
        if not url_entry:
            raise error_codes.NO_URL_FOUND

        return GetAliasResponse.from_url_entry(url_entry)

    @app.post("/v1/url")
    def post_alias(request: PostAliasRequest):
        try:
            return url_handler.add_url(alias=request.alias, url=request.url)
        except InvalidUrlError:
            raise error_codes.INVALID_URL_PROVIDED
        except InvalidAliasLengthError:
            raise error_codes.INVALID_ALIAS_LENGTH_PROVIDED
        except InvalidAliasError:
            raise error_codes.INVALID_ALIAS_PROVIDED
        except AliasAlreadyTakenError:
            raise error_codes.ALIAS_ALREADY_TAKEN
        except Exception as e:
            print(e)
            raise error_codes.INTERNAL_ERROR

    return app
