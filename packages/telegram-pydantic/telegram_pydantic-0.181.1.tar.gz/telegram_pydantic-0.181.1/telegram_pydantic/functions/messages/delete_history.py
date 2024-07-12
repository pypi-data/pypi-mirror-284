from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteHistory(BaseModel):
    """
    functions.messages.DeleteHistory
    ID: 0xb08f922a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteHistory'] = pydantic.Field(
        'functions.messages.DeleteHistory',
        alias='_'
    )

    peer: "base.InputPeer"
    max_id: int
    just_clear: typing.Optional[bool] = None
    revoke: typing.Optional[bool] = None
    min_date: typing.Optional[int] = None
    max_date: typing.Optional[int] = None
