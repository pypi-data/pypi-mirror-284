from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChatCreate(BaseModel):
    """
    types.MessageActionChatCreate
    ID: 0xbd47cbad
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChatCreate'] = pydantic.Field(
        'types.MessageActionChatCreate',
        alias='_'
    )

    title: str
    users: list[int]
