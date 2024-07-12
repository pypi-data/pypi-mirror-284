from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetDefaultHistoryTTL(BaseModel):
    """
    functions.messages.SetDefaultHistoryTTL
    ID: 0x9eb51445
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetDefaultHistoryTTL'] = pydantic.Field(
        'functions.messages.SetDefaultHistoryTTL',
        alias='_'
    )

    period: int
