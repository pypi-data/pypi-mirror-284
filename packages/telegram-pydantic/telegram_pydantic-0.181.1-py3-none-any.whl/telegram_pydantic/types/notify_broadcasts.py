from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NotifyBroadcasts(BaseModel):
    """
    types.NotifyBroadcasts
    ID: 0xd612e8ef
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NotifyBroadcasts'] = pydantic.Field(
        'types.NotifyBroadcasts',
        alias='_'
    )

