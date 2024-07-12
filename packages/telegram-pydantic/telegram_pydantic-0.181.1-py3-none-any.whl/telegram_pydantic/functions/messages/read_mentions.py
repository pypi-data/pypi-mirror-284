from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadMentions(BaseModel):
    """
    functions.messages.ReadMentions
    ID: 0x36e5bf4d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReadMentions'] = pydantic.Field(
        'functions.messages.ReadMentions',
        alias='_'
    )

    peer: "base.InputPeer"
    top_msg_id: typing.Optional[int] = None
