from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteFactCheck(BaseModel):
    """
    functions.messages.DeleteFactCheck
    ID: 0xd1da940c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteFactCheck'] = pydantic.Field(
        'functions.messages.DeleteFactCheck',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
