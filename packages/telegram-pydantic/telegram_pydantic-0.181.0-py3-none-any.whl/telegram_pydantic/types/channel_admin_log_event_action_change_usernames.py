from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeUsernames(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeUsernames
    ID: 0xf04fb3a9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeUsernames'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeUsernames',
        alias='_'
    )

    prev_value: list[str]
    new_value: list[str]
