from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetPremiumGifts(BaseModel):
    """
    types.InputStickerSetPremiumGifts
    ID: 0xc88b3b02
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetPremiumGifts'] = pydantic.Field(
        'types.InputStickerSetPremiumGifts',
        alias='_'
    )

