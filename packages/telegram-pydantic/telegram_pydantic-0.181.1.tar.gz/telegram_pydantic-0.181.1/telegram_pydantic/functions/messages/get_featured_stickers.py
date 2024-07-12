from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetFeaturedStickers(BaseModel):
    """
    functions.messages.GetFeaturedStickers
    ID: 0x64780b14
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetFeaturedStickers'] = pydantic.Field(
        'functions.messages.GetFeaturedStickers',
        alias='_'
    )

    hash: int
