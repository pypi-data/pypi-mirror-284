from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LoadAsyncGraph(BaseModel):
    """
    functions.stats.LoadAsyncGraph
    ID: 0x621d5fa0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.LoadAsyncGraph'] = pydantic.Field(
        'functions.stats.LoadAsyncGraph',
        alias='_'
    )

    token: str
    x: typing.Optional[int] = None
