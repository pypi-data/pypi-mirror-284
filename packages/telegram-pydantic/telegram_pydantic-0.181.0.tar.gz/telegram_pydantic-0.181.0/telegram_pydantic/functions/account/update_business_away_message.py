from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBusinessAwayMessage(BaseModel):
    """
    functions.account.UpdateBusinessAwayMessage
    ID: 0xa26a7fa5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateBusinessAwayMessage'] = pydantic.Field(
        'functions.account.UpdateBusinessAwayMessage',
        alias='_'
    )

    message: typing.Optional["base.InputBusinessAwayMessage"] = None
