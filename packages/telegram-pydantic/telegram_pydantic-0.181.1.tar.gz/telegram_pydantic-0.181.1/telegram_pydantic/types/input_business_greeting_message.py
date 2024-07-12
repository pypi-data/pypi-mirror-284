from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBusinessGreetingMessage(BaseModel):
    """
    types.InputBusinessGreetingMessage
    ID: 0x194cb3b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBusinessGreetingMessage'] = pydantic.Field(
        'types.InputBusinessGreetingMessage',
        alias='_'
    )

    shortcut_id: int
    recipients: "base.InputBusinessRecipients"
    no_activity_days: int
