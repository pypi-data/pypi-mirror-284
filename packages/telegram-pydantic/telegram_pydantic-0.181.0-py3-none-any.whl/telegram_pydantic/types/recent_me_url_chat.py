from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecentMeUrlChat(BaseModel):
    """
    types.RecentMeUrlChat
    ID: 0xb2da71d2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RecentMeUrlChat'] = pydantic.Field(
        'types.RecentMeUrlChat',
        alias='_'
    )

    url: str
    chat_id: int
