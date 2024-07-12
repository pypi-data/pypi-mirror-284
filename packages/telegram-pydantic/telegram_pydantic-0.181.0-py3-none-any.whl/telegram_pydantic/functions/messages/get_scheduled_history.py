from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetScheduledHistory(BaseModel):
    """
    functions.messages.GetScheduledHistory
    ID: 0xf516760b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetScheduledHistory'] = pydantic.Field(
        'functions.messages.GetScheduledHistory',
        alias='_'
    )

    peer: "base.InputPeer"
    hash: int
