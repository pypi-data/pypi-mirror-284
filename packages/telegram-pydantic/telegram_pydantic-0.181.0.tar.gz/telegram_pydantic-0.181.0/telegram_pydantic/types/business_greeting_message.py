from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessGreetingMessage(BaseModel):
    """
    types.BusinessGreetingMessage
    ID: 0xe519abab
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessGreetingMessage'] = pydantic.Field(
        'types.BusinessGreetingMessage',
        alias='_'
    )

    shortcut_id: int
    recipients: "base.BusinessRecipients"
    no_activity_days: int
