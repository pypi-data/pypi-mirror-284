from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipant(BaseModel):
    """
    types.ChannelParticipant
    ID: 0xc00c07c0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipant'] = pydantic.Field(
        'types.ChannelParticipant',
        alias='_'
    )

    user_id: int
    date: int
