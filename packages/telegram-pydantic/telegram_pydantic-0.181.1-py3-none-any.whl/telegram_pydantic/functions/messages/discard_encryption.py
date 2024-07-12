from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DiscardEncryption(BaseModel):
    """
    functions.messages.DiscardEncryption
    ID: 0xf393aea0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DiscardEncryption'] = pydantic.Field(
        'functions.messages.DiscardEncryption',
        alias='_'
    )

    chat_id: int
    delete_history: typing.Optional[bool] = None
