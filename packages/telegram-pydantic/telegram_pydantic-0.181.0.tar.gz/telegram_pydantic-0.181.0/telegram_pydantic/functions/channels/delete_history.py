from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteHistory(BaseModel):
    """
    functions.channels.DeleteHistory
    ID: 0x9baa9647
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.DeleteHistory'] = pydantic.Field(
        'functions.channels.DeleteHistory',
        alias='_'
    )

    channel: "base.InputChannel"
    max_id: int
    for_everyone: typing.Optional[bool] = None
