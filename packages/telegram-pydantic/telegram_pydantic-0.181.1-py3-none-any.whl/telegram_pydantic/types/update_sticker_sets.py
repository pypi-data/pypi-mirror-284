from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateStickerSets(BaseModel):
    """
    types.UpdateStickerSets
    ID: 0x31c24808
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateStickerSets'] = pydantic.Field(
        'types.UpdateStickerSets',
        alias='_'
    )

    masks: typing.Optional[bool] = None
    emojis: typing.Optional[bool] = None
