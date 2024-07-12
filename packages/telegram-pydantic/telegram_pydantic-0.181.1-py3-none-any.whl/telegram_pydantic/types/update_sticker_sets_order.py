from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateStickerSetsOrder(BaseModel):
    """
    types.UpdateStickerSetsOrder
    ID: 0xbb2d201
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateStickerSetsOrder'] = pydantic.Field(
        'types.UpdateStickerSetsOrder',
        alias='_'
    )

    order: list[int]
    masks: typing.Optional[bool] = None
    emojis: typing.Optional[bool] = None
