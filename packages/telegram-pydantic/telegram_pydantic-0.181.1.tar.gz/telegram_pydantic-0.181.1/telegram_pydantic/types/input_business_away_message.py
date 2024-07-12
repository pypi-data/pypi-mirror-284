from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBusinessAwayMessage(BaseModel):
    """
    types.InputBusinessAwayMessage
    ID: 0x832175e0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBusinessAwayMessage'] = pydantic.Field(
        'types.InputBusinessAwayMessage',
        alias='_'
    )

    shortcut_id: int
    schedule: "base.BusinessAwayMessageSchedule"
    recipients: "base.InputBusinessRecipients"
    offline_only: typing.Optional[bool] = None
