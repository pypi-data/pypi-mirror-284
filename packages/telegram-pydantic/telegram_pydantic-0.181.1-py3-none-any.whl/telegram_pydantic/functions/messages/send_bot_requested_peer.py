from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendBotRequestedPeer(BaseModel):
    """
    functions.messages.SendBotRequestedPeer
    ID: 0x91b2d060
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendBotRequestedPeer'] = pydantic.Field(
        'functions.messages.SendBotRequestedPeer',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    button_id: int
    requested_peers: list["base.InputPeer"]
