from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadHistory(BaseModel):
    """
    functions.messages.ReadHistory
    ID: 0xe306d3a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReadHistory'] = pydantic.Field(
        'functions.messages.ReadHistory',
        alias='_'
    )

    peer: "base.InputPeer"
    max_id: int
