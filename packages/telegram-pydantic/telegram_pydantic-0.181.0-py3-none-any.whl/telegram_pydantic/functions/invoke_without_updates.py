from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvokeWithoutUpdates(BaseModel):
    """
    functions.InvokeWithoutUpdates
    ID: 0xbf9459b7
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.InvokeWithoutUpdates'] = pydantic.Field(
        'functions.InvokeWithoutUpdates',
        alias='_'
    )

    query: BaseModel
