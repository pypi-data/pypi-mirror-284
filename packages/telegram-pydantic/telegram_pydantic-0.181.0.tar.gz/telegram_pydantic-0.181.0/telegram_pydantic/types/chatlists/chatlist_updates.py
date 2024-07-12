from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatlistUpdates(BaseModel):
    """
    types.chatlists.ChatlistUpdates
    ID: 0x93bd878d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.chatlists.ChatlistUpdates'] = pydantic.Field(
        'types.chatlists.ChatlistUpdates',
        alias='_'
    )

    missing_peers: list["base.Peer"]
    chats: list["base.Chat"]
    users: list["base.User"]
