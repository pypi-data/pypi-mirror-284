from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetOldFeaturedStickers(BaseModel):
    """
    functions.messages.GetOldFeaturedStickers
    ID: 0x7ed094a1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetOldFeaturedStickers'] = pydantic.Field(
        'functions.messages.GetOldFeaturedStickers',
        alias='_'
    )

    offset: int
    limit: int
    hash: int
