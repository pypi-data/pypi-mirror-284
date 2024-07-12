from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DifferenceSlice(BaseModel):
    """
    types.updates.DifferenceSlice
    ID: 0xa8fb1981
    Layer: 181
    """
    QUALNAME: typing.Literal['types.updates.DifferenceSlice'] = pydantic.Field(
        'types.updates.DifferenceSlice',
        alias='_'
    )

    new_messages: list["base.Message"]
    new_encrypted_messages: list["base.EncryptedMessage"]
    other_updates: list["base.Update"]
    chats: list["base.Chat"]
    users: list["base.User"]
    intermediate_state: "base.updates.State"
