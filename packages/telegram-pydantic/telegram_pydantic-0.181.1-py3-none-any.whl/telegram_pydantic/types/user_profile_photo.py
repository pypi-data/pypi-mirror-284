from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserProfilePhoto(BaseModel):
    """
    types.UserProfilePhoto
    ID: 0x82d1f706
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UserProfilePhoto'] = pydantic.Field(
        'types.UserProfilePhoto',
        alias='_'
    )

    photo_id: int
    dc_id: int
    has_video: typing.Optional[bool] = None
    personal: typing.Optional[bool] = None
    stripped_thumb: typing.Optional[bytes] = None
