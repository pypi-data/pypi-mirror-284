from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetEmojiGenericAnimations(BaseModel):
    """
    types.InputStickerSetEmojiGenericAnimations
    ID: 0x4c4d4ce
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetEmojiGenericAnimations'] = pydantic.Field(
        'types.InputStickerSetEmojiGenericAnimations',
        alias='_'
    )

