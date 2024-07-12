from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetHistoryTTL(BaseModel):
    """
    functions.messages.SetHistoryTTL
    ID: 0xb80e5fe4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetHistoryTTL'] = pydantic.Field(
        'functions.messages.SetHistoryTTL',
        alias='_'
    )

    peer: "base.InputPeer"
    period: int
