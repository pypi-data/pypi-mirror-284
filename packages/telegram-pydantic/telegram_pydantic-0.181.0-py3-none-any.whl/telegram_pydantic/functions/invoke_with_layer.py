from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvokeWithLayer(BaseModel):
    """
    functions.InvokeWithLayer
    ID: 0xda9b0d0d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.InvokeWithLayer'] = pydantic.Field(
        'functions.InvokeWithLayer',
        alias='_'
    )

    layer: int
    query: BaseModel
