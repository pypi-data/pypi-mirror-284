from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetAuthorization(BaseModel):
    """
    functions.account.ResetAuthorization
    ID: 0xdf77f3bc
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ResetAuthorization'] = pydantic.Field(
        'functions.account.ResetAuthorization',
        alias='_'
    )

    hash: int
