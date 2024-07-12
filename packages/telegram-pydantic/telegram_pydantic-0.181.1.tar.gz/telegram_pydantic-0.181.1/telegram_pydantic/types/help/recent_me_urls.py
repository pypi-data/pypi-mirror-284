from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecentMeUrls(BaseModel):
    """
    types.help.RecentMeUrls
    ID: 0xe0310d7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.RecentMeUrls'] = pydantic.Field(
        'types.help.RecentMeUrls',
        alias='_'
    )

    urls: list["base.RecentMeUrl"]
    chats: list["base.Chat"]
    users: list["base.User"]
