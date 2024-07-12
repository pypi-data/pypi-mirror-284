from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionTogglePreHistoryHidden(BaseModel):
    """
    types.ChannelAdminLogEventActionTogglePreHistoryHidden
    ID: 0x5f5c95f1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionTogglePreHistoryHidden'] = pydantic.Field(
        'types.ChannelAdminLogEventActionTogglePreHistoryHidden',
        alias='_'
    )

    new_value: bool
