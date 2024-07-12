from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WallPaperSettings(BaseModel):
    """
    types.WallPaperSettings
    ID: 0x372efcd0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WallPaperSettings'] = pydantic.Field(
        'types.WallPaperSettings',
        alias='_'
    )

    blur: typing.Optional[bool] = None
    motion: typing.Optional[bool] = None
    background_color: typing.Optional[int] = None
    second_background_color: typing.Optional[int] = None
    third_background_color: typing.Optional[int] = None
    fourth_background_color: typing.Optional[int] = None
    intensity: typing.Optional[int] = None
    rotation: typing.Optional[int] = None
    emoticon: typing.Optional[str] = None
