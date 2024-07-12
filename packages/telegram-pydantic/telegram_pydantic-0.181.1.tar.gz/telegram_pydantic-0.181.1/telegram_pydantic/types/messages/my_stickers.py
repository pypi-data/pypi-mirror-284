from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MyStickers(BaseModel):
    """
    types.messages.MyStickers
    ID: 0xfaff629d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.MyStickers'] = pydantic.Field(
        'types.messages.MyStickers',
        alias='_'
    )

    count: int
    sets: list["base.StickerSetCovered"]
