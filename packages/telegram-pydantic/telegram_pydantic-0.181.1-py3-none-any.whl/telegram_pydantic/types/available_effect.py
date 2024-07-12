from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AvailableEffect(BaseModel):
    """
    types.AvailableEffect
    ID: 0x93c3e27e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AvailableEffect'] = pydantic.Field(
        'types.AvailableEffect',
        alias='_'
    )

    id: int
    emoticon: str
    effect_sticker_id: int
    premium_required: typing.Optional[bool] = None
    static_icon_id: typing.Optional[int] = None
    effect_animation_id: typing.Optional[int] = None
