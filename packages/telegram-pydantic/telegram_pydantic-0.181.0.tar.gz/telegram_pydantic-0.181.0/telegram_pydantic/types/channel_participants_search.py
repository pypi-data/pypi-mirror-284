from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantsSearch(BaseModel):
    """
    types.ChannelParticipantsSearch
    ID: 0x656ac4b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantsSearch'] = pydantic.Field(
        'types.ChannelParticipantsSearch',
        alias='_'
    )

    q: str
