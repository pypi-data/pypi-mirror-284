from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvokeWithApnsSecret(BaseModel):
    """
    functions.InvokeWithApnsSecret
    ID: 0x0dae54f8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.InvokeWithApnsSecret'] = pydantic.Field(
        'functions.InvokeWithApnsSecret',
        alias='_'
    )

    nonce: str
    secret: str
    query: BaseModel
