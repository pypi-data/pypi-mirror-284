from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvokeAfterMsg(BaseModel):
    """
    functions.InvokeAfterMsg
    ID: 0xcb9f372d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.InvokeAfterMsg'] = pydantic.Field(
        'functions.InvokeAfterMsg',
        alias='_'
    )

    msg_id: int
    query: BaseModel
