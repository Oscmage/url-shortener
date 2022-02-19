from fastapi import FastAPI
from starlette.responses import RedirectResponse

import app.error_codes as error_codes
from app.url.handler import UrlHandler
from app.exception import InvalidUrlError, InvalidAliasLengthError, InvalidAliasError, AliasAlreadyTakenError
from app.responses import PostAliasRequest, PostAliasResponse
from app.url.interface import UrlInterface
from app.url.repository import UrlRepository
from fastapi.middleware.cors import CORSMiddleware

CORS_ORIGINS = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]


def start():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

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

        return RedirectResponse(url=url_entry.url)


    @app.post("/v1/url")
    def post_alias(request: PostAliasRequest):
        try:
            url_entry = url_handler.add_url(url=request.url, alias=request.alias)
            return PostAliasResponse.from_url_entry(url_entry)
        except InvalidUrlError:
            print("invalid url")
            raise error_codes.INVALID_URL_PROVIDED
        except InvalidAliasLengthError:
            print("invalid alias length")
            raise error_codes.INVALID_ALIAS_LENGTH_PROVIDED
        except InvalidAliasError:
            print("invalid alias")
            raise error_codes.INVALID_ALIAS_PROVIDED
        except AliasAlreadyTakenError:
            print("Alias taken")
            raise error_codes.ALIAS_ALREADY_TAKEN
        except Exception as e:
            print(e)
            raise error_codes.INTERNAL_ERROR

    return app
