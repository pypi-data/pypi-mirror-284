from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckedGiftCode(BaseModel):
    """
    types.payments.CheckedGiftCode
    ID: 0x284a1096
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.CheckedGiftCode'] = pydantic.Field(
        'types.payments.CheckedGiftCode',
        alias='_'
    )

    date: int
    months: int
    chats: list["base.Chat"]
    users: list["base.User"]
    via_giveaway: typing.Optional[bool] = None
    from_id: typing.Optional["base.Peer"] = None
    giveaway_msg_id: typing.Optional[int] = None
    to_id: typing.Optional[int] = None
    used_date: typing.Optional[int] = None
