from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JoinAsPeers(BaseModel):
    """
    types.phone.JoinAsPeers
    ID: 0xafe5623f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.phone.JoinAsPeers'] = pydantic.Field(
        'types.phone.JoinAsPeers',
        alias='_'
    )

    peers: list["base.Peer"]
    chats: list["base.Chat"]
    users: list["base.User"]
