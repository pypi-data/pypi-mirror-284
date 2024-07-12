from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StarsStatus(BaseModel):
    """
    types.payments.StarsStatus
    ID: 0x8cf4ee60
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.StarsStatus'] = pydantic.Field(
        'types.payments.StarsStatus',
        alias='_'
    )

    balance: int
    history: list["base.StarsTransaction"]
    chats: list["base.Chat"]
    users: list["base.User"]
    next_offset: typing.Optional[str] = None
