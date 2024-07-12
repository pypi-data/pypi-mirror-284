from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDefaultBackgroundEmojis(BaseModel):
    """
    functions.account.GetDefaultBackgroundEmojis
    ID: 0xa60ab9ce
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetDefaultBackgroundEmojis'] = pydantic.Field(
        'functions.account.GetDefaultBackgroundEmojis',
        alias='_'
    )

    hash: int
