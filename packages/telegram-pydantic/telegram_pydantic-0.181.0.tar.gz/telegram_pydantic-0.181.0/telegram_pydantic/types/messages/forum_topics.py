from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ForumTopics(BaseModel):
    """
    types.messages.ForumTopics
    ID: 0x367617d3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ForumTopics'] = pydantic.Field(
        'types.messages.ForumTopics',
        alias='_'
    )

    count: int
    topics: list["base.ForumTopic"]
    messages: list["base.Message"]
    chats: list["base.Chat"]
    users: list["base.User"]
    pts: int
    order_by_create_date: typing.Optional[bool] = None
