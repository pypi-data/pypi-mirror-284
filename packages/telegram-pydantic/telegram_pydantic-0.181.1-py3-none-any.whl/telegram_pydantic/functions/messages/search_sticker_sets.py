from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchStickerSets(BaseModel):
    """
    functions.messages.SearchStickerSets
    ID: 0x35705b8a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SearchStickerSets'] = pydantic.Field(
        'functions.messages.SearchStickerSets',
        alias='_'
    )

    q: str
    hash: int
    exclude_featured: typing.Optional[bool] = None
