from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionSuggestProfilePhoto(BaseModel):
    """
    types.MessageActionSuggestProfilePhoto
    ID: 0x57de635e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionSuggestProfilePhoto'] = pydantic.Field(
        'types.MessageActionSuggestProfilePhoto',
        alias='_'
    )

    photo: "base.Photo"
