from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeAbout(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeAbout
    ID: 0x55188a2e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeAbout'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeAbout',
        alias='_'
    )

    prev_value: str
    new_value: str
