from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateConnectedBot(BaseModel):
    """
    functions.account.UpdateConnectedBot
    ID: 0x43d8521d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateConnectedBot'] = pydantic.Field(
        'functions.account.UpdateConnectedBot',
        alias='_'
    )

    bot: "base.InputUser"
    recipients: "base.InputBusinessBotRecipients"
    can_reply: typing.Optional[bool] = None
    deleted: typing.Optional[bool] = None
