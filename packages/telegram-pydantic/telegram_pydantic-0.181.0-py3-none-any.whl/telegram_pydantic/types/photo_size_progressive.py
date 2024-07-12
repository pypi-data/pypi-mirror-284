from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhotoSizeProgressive(BaseModel):
    """
    types.PhotoSizeProgressive
    ID: 0xfa3efb95
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhotoSizeProgressive'] = pydantic.Field(
        'types.PhotoSizeProgressive',
        alias='_'
    )

    type: str
    w: int
    h: int
    sizes: list[int]
