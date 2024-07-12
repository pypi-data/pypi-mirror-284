from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBusinessGreetingMessage(BaseModel):
    """
    functions.account.UpdateBusinessGreetingMessage
    ID: 0x66cdafc4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateBusinessGreetingMessage'] = pydantic.Field(
        'functions.account.UpdateBusinessGreetingMessage',
        alias='_'
    )

    message: typing.Optional["base.InputBusinessGreetingMessage"] = None
