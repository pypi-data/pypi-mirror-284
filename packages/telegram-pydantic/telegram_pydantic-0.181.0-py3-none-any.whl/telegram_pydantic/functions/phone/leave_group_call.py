from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LeaveGroupCall(BaseModel):
    """
    functions.phone.LeaveGroupCall
    ID: 0x500377f9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.LeaveGroupCall'] = pydantic.Field(
        'functions.phone.LeaveGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
    source: int
