from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessChatLinks(BaseModel):
    """
    types.account.BusinessChatLinks
    ID: 0xec43a2d1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.BusinessChatLinks'] = pydantic.Field(
        'types.account.BusinessChatLinks',
        alias='_'
    )

    links: list["base.BusinessChatLink"]
    chats: list["base.Chat"]
    users: list["base.User"]
