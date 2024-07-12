from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPhotoLegacyFileLocation(BaseModel):
    """
    types.InputPhotoLegacyFileLocation
    ID: 0xd83466f3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPhotoLegacyFileLocation'] = pydantic.Field(
        'types.InputPhotoLegacyFileLocation',
        alias='_'
    )

    id: int
    access_hash: int
    file_reference: bytes
    volume_id: int
    local_id: int
    secret: int
