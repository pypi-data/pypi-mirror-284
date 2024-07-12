from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendVote(BaseModel):
    """
    functions.messages.SendVote
    ID: 0x10ea6184
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendVote'] = pydantic.Field(
        'functions.messages.SendVote',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    options: list[bytes]
