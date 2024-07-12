from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResolvedPeer(BaseModel):
    """
    types.contacts.ResolvedPeer
    ID: 0x7f077ad9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.ResolvedPeer'] = pydantic.Field(
        'types.contacts.ResolvedPeer',
        alias='_'
    )

    peer: "base.Peer"
    chats: list["base.Chat"]
    users: list["base.User"]
