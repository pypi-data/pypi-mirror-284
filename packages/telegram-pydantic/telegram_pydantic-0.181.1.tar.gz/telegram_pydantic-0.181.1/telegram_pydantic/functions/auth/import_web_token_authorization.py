from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ImportWebTokenAuthorization(BaseModel):
    """
    functions.auth.ImportWebTokenAuthorization
    ID: 0x2db873a9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.ImportWebTokenAuthorization'] = pydantic.Field(
        'functions.auth.ImportWebTokenAuthorization',
        alias='_'
    )

    api_id: int
    api_hash: str
    web_auth_token: str
