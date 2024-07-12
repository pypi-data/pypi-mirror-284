from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionGiveawayResults(BaseModel):
    """
    types.MessageActionGiveawayResults
    ID: 0x2a9fadc5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionGiveawayResults'] = pydantic.Field(
        'types.MessageActionGiveawayResults',
        alias='_'
    )

    winners_count: int
    unclaimed_count: int
