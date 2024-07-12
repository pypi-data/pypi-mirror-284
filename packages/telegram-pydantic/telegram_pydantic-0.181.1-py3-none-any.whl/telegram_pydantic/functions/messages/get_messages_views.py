from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMessagesViews(BaseModel):
    """
    functions.messages.GetMessagesViews
    ID: 0x5784d3e1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetMessagesViews'] = pydantic.Field(
        'functions.messages.GetMessagesViews',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
    increment: bool
