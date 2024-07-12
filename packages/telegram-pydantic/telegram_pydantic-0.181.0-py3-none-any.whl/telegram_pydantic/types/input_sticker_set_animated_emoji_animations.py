from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetAnimatedEmojiAnimations(BaseModel):
    """
    types.InputStickerSetAnimatedEmojiAnimations
    ID: 0xcde3739
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetAnimatedEmojiAnimations'] = pydantic.Field(
        'types.InputStickerSetAnimatedEmojiAnimations',
        alias='_'
    )

