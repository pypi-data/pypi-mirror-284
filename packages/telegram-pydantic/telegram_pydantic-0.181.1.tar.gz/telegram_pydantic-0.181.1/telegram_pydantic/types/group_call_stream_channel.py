from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GroupCallStreamChannel(BaseModel):
    """
    types.GroupCallStreamChannel
    ID: 0x80eb48af
    Layer: 181
    """
    QUALNAME: typing.Literal['types.GroupCallStreamChannel'] = pydantic.Field(
        'types.GroupCallStreamChannel',
        alias='_'
    )

    channel: int
    scale: int
    last_timestamp_ms: int
