from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotPrecheckoutQuery(BaseModel):
    """
    types.UpdateBotPrecheckoutQuery
    ID: 0x8caa9a96
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotPrecheckoutQuery'] = pydantic.Field(
        'types.UpdateBotPrecheckoutQuery',
        alias='_'
    )

    query_id: int
    user_id: int
    payload: bytes
    currency: str
    total_amount: int
    info: typing.Optional["base.PaymentRequestedInfo"] = None
    shipping_option_id: typing.Optional[str] = None
