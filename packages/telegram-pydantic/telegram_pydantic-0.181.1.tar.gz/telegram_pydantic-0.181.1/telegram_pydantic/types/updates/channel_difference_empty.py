from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelDifferenceEmpty(BaseModel):
    """
    types.updates.ChannelDifferenceEmpty
    ID: 0x3e11affb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.updates.ChannelDifferenceEmpty'] = pydantic.Field(
        'types.updates.ChannelDifferenceEmpty',
        alias='_'
    )

    pts: int
    final: typing.Optional[bool] = None
    timeout: typing.Optional[int] = None
