from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatInviteAlready(BaseModel):
    """
    types.ChatInviteAlready
    ID: 0x5a686d7c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatInviteAlready'] = pydantic.Field(
        'types.ChatInviteAlready',
        alias='_'
    )

    chat: "base.Chat"
