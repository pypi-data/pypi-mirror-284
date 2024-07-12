from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDiscussionMessage(BaseModel):
    """
    functions.messages.GetDiscussionMessage
    ID: 0x446972fd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDiscussionMessage'] = pydantic.Field(
        'functions.messages.GetDiscussionMessage',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
