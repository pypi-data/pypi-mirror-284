from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionToggleForum(BaseModel):
    """
    types.ChannelAdminLogEventActionToggleForum
    ID: 0x2cc6383
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionToggleForum'] = pydantic.Field(
        'types.ChannelAdminLogEventActionToggleForum',
        alias='_'
    )

    new_value: bool
