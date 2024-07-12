from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateProfilePhoto(BaseModel):
    """
    functions.photos.UpdateProfilePhoto
    ID: 0x9e82039
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.photos.UpdateProfilePhoto'] = pydantic.Field(
        'functions.photos.UpdateProfilePhoto',
        alias='_'
    )

    id: "base.InputPhoto"
    fallback: typing.Optional[bool] = None
    bot: typing.Optional["base.InputUser"] = None
