from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNewScheduledMessage(BaseModel):
    """
    types.UpdateNewScheduledMessage
    ID: 0x39a51dfb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateNewScheduledMessage'] = pydantic.Field(
        'types.UpdateNewScheduledMessage',
        alias='_'
    )

    message: "base.Message"
