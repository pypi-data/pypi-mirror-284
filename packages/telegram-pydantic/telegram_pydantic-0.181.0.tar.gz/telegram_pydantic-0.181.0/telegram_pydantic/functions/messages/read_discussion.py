from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadDiscussion(BaseModel):
    """
    functions.messages.ReadDiscussion
    ID: 0xf731a9f4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReadDiscussion'] = pydantic.Field(
        'functions.messages.ReadDiscussion',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    read_max_id: int
