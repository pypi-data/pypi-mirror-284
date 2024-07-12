from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ArchivedStickers(BaseModel):
    """
    types.messages.ArchivedStickers
    ID: 0x4fcba9c8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ArchivedStickers'] = pydantic.Field(
        'types.messages.ArchivedStickers',
        alias='_'
    )

    count: int
    sets: list["base.StickerSetCovered"]
