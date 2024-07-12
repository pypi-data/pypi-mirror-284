from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChatEditPhoto(BaseModel):
    """
    types.MessageActionChatEditPhoto
    ID: 0x7fcb13a8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChatEditPhoto'] = pydantic.Field(
        'types.MessageActionChatEditPhoto',
        alias='_'
    )

    photo: "base.Photo"
