from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetEmojiStickerGroups(BaseModel):
    """
    functions.messages.GetEmojiStickerGroups
    ID: 0x1dd840f5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetEmojiStickerGroups'] = pydantic.Field(
        'functions.messages.GetEmojiStickerGroups',
        alias='_'
    )

    hash: int
