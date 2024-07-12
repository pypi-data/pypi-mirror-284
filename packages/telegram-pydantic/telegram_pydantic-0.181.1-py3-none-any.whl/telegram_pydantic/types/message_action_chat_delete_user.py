from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChatDeleteUser(BaseModel):
    """
    types.MessageActionChatDeleteUser
    ID: 0xa43f30cc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChatDeleteUser'] = pydantic.Field(
        'types.MessageActionChatDeleteUser',
        alias='_'
    )

    user_id: int
