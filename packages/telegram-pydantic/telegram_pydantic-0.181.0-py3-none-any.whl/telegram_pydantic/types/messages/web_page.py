from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebPage(BaseModel):
    """
    types.messages.WebPage
    ID: 0xfd5e12bd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.WebPage'] = pydantic.Field(
        'types.messages.WebPage',
        alias='_'
    )

    webpage: "base.WebPage"
    chats: list["base.Chat"]
    users: list["base.User"]
