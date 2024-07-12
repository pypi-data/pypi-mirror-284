from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvokeWithMessagesRange(BaseModel):
    """
    functions.InvokeWithMessagesRange
    ID: 0x365275f2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.InvokeWithMessagesRange'] = pydantic.Field(
        'functions.InvokeWithMessagesRange',
        alias='_'
    )

    range: "base.MessageRange"
    query: BaseModel
