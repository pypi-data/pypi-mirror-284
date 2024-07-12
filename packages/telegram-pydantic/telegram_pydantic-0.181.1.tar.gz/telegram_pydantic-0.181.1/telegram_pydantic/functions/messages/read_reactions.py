from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadReactions(BaseModel):
    """
    functions.messages.ReadReactions
    ID: 0x54aa7f8e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReadReactions'] = pydantic.Field(
        'functions.messages.ReadReactions',
        alias='_'
    )

    peer: "base.InputPeer"
    top_msg_id: typing.Optional[int] = None
