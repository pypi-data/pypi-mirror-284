from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleViewForumAsMessages(BaseModel):
    """
    functions.channels.ToggleViewForumAsMessages
    ID: 0x9738bb15
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleViewForumAsMessages'] = pydantic.Field(
        'functions.channels.ToggleViewForumAsMessages',
        alias='_'
    )

    channel: "base.InputChannel"
    enabled: bool
