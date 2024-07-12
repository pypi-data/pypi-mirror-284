from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeers(BaseModel):
    """
    types.contacts.TopPeers
    ID: 0x70b772a8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.TopPeers'] = pydantic.Field(
        'types.contacts.TopPeers',
        alias='_'
    )

    categories: list["base.TopPeerCategoryPeers"]
    chats: list["base.Chat"]
    users: list["base.User"]
