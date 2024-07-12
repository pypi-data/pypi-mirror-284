from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChatDeletePhoto(BaseModel):
    """
    types.MessageActionChatDeletePhoto
    ID: 0x95e3fbef
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChatDeletePhoto'] = pydantic.Field(
        'types.MessageActionChatDeletePhoto',
        alias='_'
    )

