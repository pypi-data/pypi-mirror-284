from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuBotsBot(BaseModel):
    """
    types.AttachMenuBotsBot
    ID: 0x93bf667f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuBotsBot'] = pydantic.Field(
        'types.AttachMenuBotsBot',
        alias='_'
    )

    bot: "base.AttachMenuBot"
    users: list["base.User"]
