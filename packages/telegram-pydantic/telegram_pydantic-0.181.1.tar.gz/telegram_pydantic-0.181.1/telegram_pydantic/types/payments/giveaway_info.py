from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GiveawayInfo(BaseModel):
    """
    types.payments.GiveawayInfo
    ID: 0x4367daa0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.GiveawayInfo'] = pydantic.Field(
        'types.payments.GiveawayInfo',
        alias='_'
    )

    start_date: int
    participating: typing.Optional[bool] = None
    preparing_results: typing.Optional[bool] = None
    joined_too_early_date: typing.Optional[int] = None
    admin_disallowed_chat_id: typing.Optional[int] = None
    disallowed_country: typing.Optional[str] = None
