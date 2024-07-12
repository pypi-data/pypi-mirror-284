from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannel(BaseModel):
    """
    types.UpdateChannel
    ID: 0x635b4c09
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannel'] = pydantic.Field(
        'types.UpdateChannel',
        alias='_'
    )

    channel_id: int
