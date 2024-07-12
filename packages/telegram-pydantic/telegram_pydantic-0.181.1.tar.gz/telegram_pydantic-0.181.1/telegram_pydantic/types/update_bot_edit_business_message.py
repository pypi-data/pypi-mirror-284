from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotEditBusinessMessage(BaseModel):
    """
    types.UpdateBotEditBusinessMessage
    ID: 0x7df587c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotEditBusinessMessage'] = pydantic.Field(
        'types.UpdateBotEditBusinessMessage',
        alias='_'
    )

    connection_id: str
    message: "base.Message"
    qts: int
    reply_to_message: typing.Optional["base.Message"] = None
