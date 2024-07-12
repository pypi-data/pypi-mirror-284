from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGroupCall(BaseModel):
    """
    functions.phone.GetGroupCall
    ID: 0x41845db
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.GetGroupCall'] = pydantic.Field(
        'functions.phone.GetGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
    limit: int
