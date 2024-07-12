from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteSavedHistory(BaseModel):
    """
    functions.messages.DeleteSavedHistory
    ID: 0x6e98102b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteSavedHistory'] = pydantic.Field(
        'functions.messages.DeleteSavedHistory',
        alias='_'
    )

    peer: "base.InputPeer"
    max_id: int
    min_date: typing.Optional[int] = None
    max_date: typing.Optional[int] = None
