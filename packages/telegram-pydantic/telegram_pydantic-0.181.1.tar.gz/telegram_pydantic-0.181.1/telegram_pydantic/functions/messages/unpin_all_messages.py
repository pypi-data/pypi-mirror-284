from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UnpinAllMessages(BaseModel):
    """
    functions.messages.UnpinAllMessages
    ID: 0xee22b9a8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.UnpinAllMessages'] = pydantic.Field(
        'functions.messages.UnpinAllMessages',
        alias='_'
    )

    peer: "base.InputPeer"
    top_msg_id: typing.Optional[int] = None
