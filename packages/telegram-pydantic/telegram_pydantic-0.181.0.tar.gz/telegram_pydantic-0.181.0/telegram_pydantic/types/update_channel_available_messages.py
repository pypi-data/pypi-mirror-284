from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannelAvailableMessages(BaseModel):
    """
    types.UpdateChannelAvailableMessages
    ID: 0xb23fc698
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannelAvailableMessages'] = pydantic.Field(
        'types.UpdateChannelAvailableMessages',
        alias='_'
    )

    channel_id: int
    available_min_id: int
