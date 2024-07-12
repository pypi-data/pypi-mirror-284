from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleBotInAttachMenu(BaseModel):
    """
    functions.messages.ToggleBotInAttachMenu
    ID: 0x69f59d69
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ToggleBotInAttachMenu'] = pydantic.Field(
        'functions.messages.ToggleBotInAttachMenu',
        alias='_'
    )

    bot: "base.InputUser"
    enabled: bool
    write_allowed: typing.Optional[bool] = None
