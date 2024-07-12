from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetFactCheck(BaseModel):
    """
    functions.messages.GetFactCheck
    ID: 0xb9cdc5ee
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetFactCheck'] = pydantic.Field(
        'functions.messages.GetFactCheck',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: list[int]
