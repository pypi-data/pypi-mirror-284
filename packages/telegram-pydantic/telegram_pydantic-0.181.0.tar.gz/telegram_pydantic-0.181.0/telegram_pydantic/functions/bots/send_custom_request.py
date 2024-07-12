from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendCustomRequest(BaseModel):
    """
    functions.bots.SendCustomRequest
    ID: 0xaa2769ed
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.SendCustomRequest'] = pydantic.Field(
        'functions.bots.SendCustomRequest',
        alias='_'
    )

    custom_method: str
    params: "base.DataJSON"
