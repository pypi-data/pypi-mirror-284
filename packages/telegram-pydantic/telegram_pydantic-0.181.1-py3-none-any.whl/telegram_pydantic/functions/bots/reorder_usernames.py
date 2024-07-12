from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReorderUsernames(BaseModel):
    """
    functions.bots.ReorderUsernames
    ID: 0x9709b1c2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.ReorderUsernames'] = pydantic.Field(
        'functions.bots.ReorderUsernames',
        alias='_'
    )

    bot: "base.InputUser"
    order: list[str]
