from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetWebAuthorization(BaseModel):
    """
    functions.account.ResetWebAuthorization
    ID: 0x2d01b9ef
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ResetWebAuthorization'] = pydantic.Field(
        'functions.account.ResetWebAuthorization',
        alias='_'
    )

    hash: int
