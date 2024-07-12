from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvokeWithBusinessConnection(BaseModel):
    """
    functions.InvokeWithBusinessConnection
    ID: 0xdd289f8e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.InvokeWithBusinessConnection'] = pydantic.Field(
        'functions.InvokeWithBusinessConnection',
        alias='_'
    )

    connection_id: str
    query: BaseModel
