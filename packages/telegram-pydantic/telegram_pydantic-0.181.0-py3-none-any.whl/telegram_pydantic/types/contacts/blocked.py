from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Blocked(BaseModel):
    """
    types.contacts.Blocked
    ID: 0xade1591
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.Blocked'] = pydantic.Field(
        'types.contacts.Blocked',
        alias='_'
    )

    blocked: list["base.PeerBlocked"]
    chats: list["base.Chat"]
    users: list["base.User"]
