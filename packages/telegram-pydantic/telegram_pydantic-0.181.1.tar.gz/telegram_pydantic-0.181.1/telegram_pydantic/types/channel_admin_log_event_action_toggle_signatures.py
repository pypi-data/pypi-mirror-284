from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionToggleSignatures(BaseModel):
    """
    types.ChannelAdminLogEventActionToggleSignatures
    ID: 0x26ae0971
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionToggleSignatures'] = pydantic.Field(
        'types.ChannelAdminLogEventActionToggleSignatures',
        alias='_'
    )

    new_value: bool
