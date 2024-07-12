from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerDialogs(BaseModel):
    """
    types.messages.PeerDialogs
    ID: 0x3371c354
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.PeerDialogs'] = pydantic.Field(
        'types.messages.PeerDialogs',
        alias='_'
    )

    dialogs: list["base.Dialog"]
    messages: list["base.Message"]
    chats: list["base.Chat"]
    users: list["base.User"]
    state: "base.updates.State"
