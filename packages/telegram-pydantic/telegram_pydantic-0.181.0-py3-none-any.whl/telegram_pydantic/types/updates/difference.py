from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Difference(BaseModel):
    """
    types.updates.Difference
    ID: 0xf49ca0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.updates.Difference'] = pydantic.Field(
        'types.updates.Difference',
        alias='_'
    )

    new_messages: list["base.Message"]
    new_encrypted_messages: list["base.EncryptedMessage"]
    other_updates: list["base.Update"]
    chats: list["base.Chat"]
    users: list["base.User"]
    state: "base.updates.State"
