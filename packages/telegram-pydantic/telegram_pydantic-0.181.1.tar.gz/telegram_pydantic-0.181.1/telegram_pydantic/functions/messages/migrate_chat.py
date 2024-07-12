from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MigrateChat(BaseModel):
    """
    functions.messages.MigrateChat
    ID: 0xa2875319
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.MigrateChat'] = pydantic.Field(
        'functions.messages.MigrateChat',
        alias='_'
    )

    chat_id: int
