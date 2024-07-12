from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteMessages(BaseModel):
    """
    functions.messages.DeleteMessages
    ID: 0xe58e95d2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteMessages'] = pydantic.Field(
        'functions.messages.DeleteMessages',
        alias='_'
    )

    id: list[int]
    revoke: typing.Optional[bool] = None
