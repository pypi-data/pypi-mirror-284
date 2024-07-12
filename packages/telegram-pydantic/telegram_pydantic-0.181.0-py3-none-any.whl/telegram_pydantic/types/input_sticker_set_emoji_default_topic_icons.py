from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetEmojiDefaultTopicIcons(BaseModel):
    """
    types.InputStickerSetEmojiDefaultTopicIcons
    ID: 0x44c1f8e9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetEmojiDefaultTopicIcons'] = pydantic.Field(
        'types.InputStickerSetEmojiDefaultTopicIcons',
        alias='_'
    )

