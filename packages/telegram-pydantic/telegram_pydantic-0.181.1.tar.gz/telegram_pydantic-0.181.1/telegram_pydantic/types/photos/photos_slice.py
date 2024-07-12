from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhotosSlice(BaseModel):
    """
    types.photos.PhotosSlice
    ID: 0x15051f54
    Layer: 181
    """
    QUALNAME: typing.Literal['types.photos.PhotosSlice'] = pydantic.Field(
        'types.photos.PhotosSlice',
        alias='_'
    )

    count: int
    photos: list["base.Photo"]
    users: list["base.User"]
