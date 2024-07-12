from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadEncryptedHistory(BaseModel):
    """
    functions.messages.ReadEncryptedHistory
    ID: 0x7f4b690a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReadEncryptedHistory'] = pydantic.Field(
        'functions.messages.ReadEncryptedHistory',
        alias='_'
    )

    peer: "base.InputEncryptedChat"
    max_date: int
