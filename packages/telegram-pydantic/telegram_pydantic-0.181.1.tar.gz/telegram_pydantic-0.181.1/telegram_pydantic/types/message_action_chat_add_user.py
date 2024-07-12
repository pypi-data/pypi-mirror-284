from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChatAddUser(BaseModel):
    """
    types.MessageActionChatAddUser
    ID: 0x15cefd00
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChatAddUser'] = pydantic.Field(
        'types.MessageActionChatAddUser',
        alias='_'
    )

    users: list[int]
