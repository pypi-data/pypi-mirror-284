from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeUsername(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeUsername
    ID: 0x6a4afc38
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeUsername'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeUsername',
        alias='_'
    )

    prev_value: str
    new_value: str
