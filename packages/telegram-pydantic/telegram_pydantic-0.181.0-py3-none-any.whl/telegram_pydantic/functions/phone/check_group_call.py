from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckGroupCall(BaseModel):
    """
    functions.phone.CheckGroupCall
    ID: 0xb59cf977
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.CheckGroupCall'] = pydantic.Field(
        'functions.phone.CheckGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
    sources: list[int]
