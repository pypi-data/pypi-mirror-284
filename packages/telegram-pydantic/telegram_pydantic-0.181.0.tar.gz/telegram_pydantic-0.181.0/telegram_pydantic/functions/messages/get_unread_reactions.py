from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetUnreadReactions(BaseModel):
    """
    functions.messages.GetUnreadReactions
    ID: 0x3223495b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetUnreadReactions'] = pydantic.Field(
        'functions.messages.GetUnreadReactions',
        alias='_'
    )

    peer: "base.InputPeer"
    offset_id: int
    add_offset: int
    limit: int
    max_id: int
    min_id: int
    top_msg_id: typing.Optional[int] = None
