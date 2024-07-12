from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPhotoFileLocation(BaseModel):
    """
    types.InputPhotoFileLocation
    ID: 0x40181ffe
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPhotoFileLocation'] = pydantic.Field(
        'types.InputPhotoFileLocation',
        alias='_'
    )

    id: int
    access_hash: int
    file_reference: bytes
    thumb_size: str
