from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvokeWithTakeout(BaseModel):
    """
    functions.InvokeWithTakeout
    ID: 0xaca9fd2e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.InvokeWithTakeout'] = pydantic.Field(
        'functions.InvokeWithTakeout',
        alias='_'
    )

    takeout_id: int
    query: BaseModel
