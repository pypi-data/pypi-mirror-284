from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetTheme(BaseModel):
    """
    functions.account.GetTheme
    ID: 0x3a5869ec
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetTheme'] = pydantic.Field(
        'functions.account.GetTheme',
        alias='_'
    )

    format: str
    theme: "base.InputTheme"
