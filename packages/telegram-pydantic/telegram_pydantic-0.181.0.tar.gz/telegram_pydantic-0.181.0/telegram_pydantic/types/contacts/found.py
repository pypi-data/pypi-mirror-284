from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Found(BaseModel):
    """
    types.contacts.Found
    ID: 0xb3134d9d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.Found'] = pydantic.Field(
        'types.contacts.Found',
        alias='_'
    )

    my_results: list["base.Peer"]
    results: list["base.Peer"]
    chats: list["base.Chat"]
    users: list["base.User"]
