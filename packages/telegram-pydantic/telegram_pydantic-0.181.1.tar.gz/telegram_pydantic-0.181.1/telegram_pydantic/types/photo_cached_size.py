from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhotoCachedSize(BaseModel):
    """
    types.PhotoCachedSize
    ID: 0x21e1ad6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhotoCachedSize'] = pydantic.Field(
        'types.PhotoCachedSize',
        alias='_'
    )

    type: str
    w: int
    h: int
    bytes: bytes
