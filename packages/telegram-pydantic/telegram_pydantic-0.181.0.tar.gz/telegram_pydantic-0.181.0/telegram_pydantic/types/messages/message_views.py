from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageViews(BaseModel):
    """
    types.messages.MessageViews
    ID: 0xb6c4f543
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.MessageViews'] = pydantic.Field(
        'types.messages.MessageViews',
        alias='_'
    )

    views: list["base.MessageViews"]
    chats: list["base.Chat"]
    users: list["base.User"]
