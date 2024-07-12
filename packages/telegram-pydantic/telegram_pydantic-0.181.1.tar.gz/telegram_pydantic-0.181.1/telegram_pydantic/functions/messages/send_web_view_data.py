from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendWebViewData(BaseModel):
    """
    functions.messages.SendWebViewData
    ID: 0xdc0242c8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendWebViewData'] = pydantic.Field(
        'functions.messages.SendWebViewData',
        alias='_'
    )

    bot: "base.InputUser"
    random_id: int
    button_text: str
    data: str
