from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhotoSize(BaseModel):
    """
    types.PhotoSize
    ID: 0x75c78e60
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhotoSize'] = pydantic.Field(
        'types.PhotoSize',
        alias='_'
    )

    type: str
    w: int
    h: int
    size: int
