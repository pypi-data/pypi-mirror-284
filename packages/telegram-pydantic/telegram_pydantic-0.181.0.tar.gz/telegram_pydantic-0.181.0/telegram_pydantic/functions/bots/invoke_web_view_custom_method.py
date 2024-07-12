from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvokeWebViewCustomMethod(BaseModel):
    """
    functions.bots.InvokeWebViewCustomMethod
    ID: 0x87fc5e7
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.InvokeWebViewCustomMethod'] = pydantic.Field(
        'functions.bots.InvokeWebViewCustomMethod',
        alias='_'
    )

    bot: "base.InputUser"
    custom_method: str
    params: "base.DataJSON"
