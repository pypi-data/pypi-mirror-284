from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetAnimatedEmoji(BaseModel):
    """
    types.InputStickerSetAnimatedEmoji
    ID: 0x28703c8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetAnimatedEmoji'] = pydantic.Field(
        'types.InputStickerSetAnimatedEmoji',
        alias='_'
    )

