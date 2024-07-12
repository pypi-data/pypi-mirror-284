from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ImportLoginToken(BaseModel):
    """
    functions.auth.ImportLoginToken
    ID: 0x95ac5ce4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.ImportLoginToken'] = pydantic.Field(
        'functions.auth.ImportLoginToken',
        alias='_'
    )

    token: bytes
