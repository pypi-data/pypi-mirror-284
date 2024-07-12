from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatesCombined(BaseModel):
    """
    types.UpdatesCombined
    ID: 0x725b04c3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatesCombined'] = pydantic.Field(
        'types.UpdatesCombined',
        alias='_'
    )

    updates: list["base.Update"]
    users: list["base.User"]
    chats: list["base.Chat"]
    date: int
    seq_start: int
    seq: int
