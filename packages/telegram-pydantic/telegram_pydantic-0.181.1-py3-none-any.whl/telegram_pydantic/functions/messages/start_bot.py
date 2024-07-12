from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StartBot(BaseModel):
    """
    functions.messages.StartBot
    ID: 0xe6df7378
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.StartBot'] = pydantic.Field(
        'functions.messages.StartBot',
        alias='_'
    )

    bot: "base.InputUser"
    peer: "base.InputPeer"
    random_id: int
    start_param: str
