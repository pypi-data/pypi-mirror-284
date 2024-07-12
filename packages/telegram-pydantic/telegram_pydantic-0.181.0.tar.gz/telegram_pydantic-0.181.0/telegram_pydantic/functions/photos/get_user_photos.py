from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetUserPhotos(BaseModel):
    """
    functions.photos.GetUserPhotos
    ID: 0x91cd32a8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.photos.GetUserPhotos'] = pydantic.Field(
        'functions.photos.GetUserPhotos',
        alias='_'
    )

    user_id: "base.InputUser"
    offset: int
    max_id: int
    limit: int
