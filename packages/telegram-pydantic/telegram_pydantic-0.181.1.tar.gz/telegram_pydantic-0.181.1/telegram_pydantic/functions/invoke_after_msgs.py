from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvokeAfterMsgs(BaseModel):
    """
    functions.InvokeAfterMsgs
    ID: 0x3dc4b4f0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.InvokeAfterMsgs'] = pydantic.Field(
        'functions.InvokeAfterMsgs',
        alias='_'
    )

    msg_ids: list[int]
    query: BaseModel
