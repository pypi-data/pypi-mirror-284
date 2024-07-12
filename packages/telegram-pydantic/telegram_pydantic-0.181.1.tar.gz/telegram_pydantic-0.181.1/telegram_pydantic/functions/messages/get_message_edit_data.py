from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMessageEditData(BaseModel):
    """
    functions.messages.GetMessageEditData
    ID: 0xfda68d36
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetMessageEditData'] = pydantic.Field(
        'functions.messages.GetMessageEditData',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
