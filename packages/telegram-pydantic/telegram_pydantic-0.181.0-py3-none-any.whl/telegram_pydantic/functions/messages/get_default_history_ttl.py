from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDefaultHistoryTTL(BaseModel):
    """
    functions.messages.GetDefaultHistoryTTL
    ID: 0x658b7188
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDefaultHistoryTTL'] = pydantic.Field(
        'functions.messages.GetDefaultHistoryTTL',
        alias='_'
    )

