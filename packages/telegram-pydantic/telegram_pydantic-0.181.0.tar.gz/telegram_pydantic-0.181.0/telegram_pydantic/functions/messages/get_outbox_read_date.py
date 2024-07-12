from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetOutboxReadDate(BaseModel):
    """
    functions.messages.GetOutboxReadDate
    ID: 0x8c4bfe5d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetOutboxReadDate'] = pydantic.Field(
        'functions.messages.GetOutboxReadDate',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
