from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadFeaturedEmojiStickers(BaseModel):
    """
    types.UpdateReadFeaturedEmojiStickers
    ID: 0xfb4c496c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadFeaturedEmojiStickers'] = pydantic.Field(
        'types.UpdateReadFeaturedEmojiStickers',
        alias='_'
    )

