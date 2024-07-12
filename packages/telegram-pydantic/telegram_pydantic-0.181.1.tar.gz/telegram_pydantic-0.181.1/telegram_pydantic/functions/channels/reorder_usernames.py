from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReorderUsernames(BaseModel):
    """
    functions.channels.ReorderUsernames
    ID: 0xb45ced1d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ReorderUsernames'] = pydantic.Field(
        'functions.channels.ReorderUsernames',
        alias='_'
    )

    channel: "base.InputChannel"
    order: list[str]
