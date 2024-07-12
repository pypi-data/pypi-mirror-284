from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleNoForwards(BaseModel):
    """
    functions.messages.ToggleNoForwards
    ID: 0xb11eafa2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ToggleNoForwards'] = pydantic.Field(
        'functions.messages.ToggleNoForwards',
        alias='_'
    )

    peer: "base.InputPeer"
    enabled: bool
