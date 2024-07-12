from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetAuthorizations(BaseModel):
    """
    functions.auth.ResetAuthorizations
    ID: 0x9fab0d1a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.ResetAuthorizations'] = pydantic.Field(
        'functions.auth.ResetAuthorizations',
        alias='_'
    )

