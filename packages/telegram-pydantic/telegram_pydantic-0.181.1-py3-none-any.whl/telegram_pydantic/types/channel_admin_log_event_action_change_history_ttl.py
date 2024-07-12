from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeHistoryTTL(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeHistoryTTL
    ID: 0x6e941a38
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeHistoryTTL'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeHistoryTTL',
        alias='_'
    )

    prev_value: int
    new_value: int
