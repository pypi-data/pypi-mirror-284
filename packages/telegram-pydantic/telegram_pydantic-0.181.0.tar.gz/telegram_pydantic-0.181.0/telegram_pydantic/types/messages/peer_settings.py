from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerSettings(BaseModel):
    """
    types.messages.PeerSettings
    ID: 0x6880b94d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.PeerSettings'] = pydantic.Field(
        'types.messages.PeerSettings',
        alias='_'
    )

    settings: "base.PeerSettings"
    chats: list["base.Chat"]
    users: list["base.User"]
