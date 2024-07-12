from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionToggleNoForwards(BaseModel):
    """
    types.ChannelAdminLogEventActionToggleNoForwards
    ID: 0xcb2ac766
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionToggleNoForwards'] = pydantic.Field(
        'types.ChannelAdminLogEventActionToggleNoForwards',
        alias='_'
    )

    new_value: bool
