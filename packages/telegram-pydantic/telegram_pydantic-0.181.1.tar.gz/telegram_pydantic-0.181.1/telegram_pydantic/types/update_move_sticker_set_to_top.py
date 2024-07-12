from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateMoveStickerSetToTop(BaseModel):
    """
    types.UpdateMoveStickerSetToTop
    ID: 0x86fccf85
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateMoveStickerSetToTop'] = pydantic.Field(
        'types.UpdateMoveStickerSetToTop',
        alias='_'
    )

    stickerset: int
    masks: typing.Optional[bool] = None
    emojis: typing.Optional[bool] = None
