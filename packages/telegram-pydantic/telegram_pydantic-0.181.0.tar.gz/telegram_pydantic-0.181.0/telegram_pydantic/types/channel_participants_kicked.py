from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantsKicked(BaseModel):
    """
    types.ChannelParticipantsKicked
    ID: 0xa3b54985
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantsKicked'] = pydantic.Field(
        'types.ChannelParticipantsKicked',
        alias='_'
    )

    q: str
