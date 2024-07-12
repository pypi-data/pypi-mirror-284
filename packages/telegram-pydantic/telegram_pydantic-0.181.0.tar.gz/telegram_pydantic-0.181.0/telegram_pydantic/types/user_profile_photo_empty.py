from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserProfilePhotoEmpty(BaseModel):
    """
    types.UserProfilePhotoEmpty
    ID: 0x4f11bae1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UserProfilePhotoEmpty'] = pydantic.Field(
        'types.UserProfilePhotoEmpty',
        alias='_'
    )

