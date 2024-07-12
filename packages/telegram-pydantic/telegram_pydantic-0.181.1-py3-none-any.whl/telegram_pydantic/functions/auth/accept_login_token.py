from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AcceptLoginToken(BaseModel):
    """
    functions.auth.AcceptLoginToken
    ID: 0xe894ad4d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.AcceptLoginToken'] = pydantic.Field(
        'functions.auth.AcceptLoginToken',
        alias='_'
    )

    token: bytes
