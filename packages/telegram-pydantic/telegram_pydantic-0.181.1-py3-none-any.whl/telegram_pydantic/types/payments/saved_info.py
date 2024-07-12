from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedInfo(BaseModel):
    """
    types.payments.SavedInfo
    ID: 0xfb8fe43c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.SavedInfo'] = pydantic.Field(
        'types.payments.SavedInfo',
        alias='_'
    )

    has_saved_credentials: typing.Optional[bool] = None
    saved_info: typing.Optional["base.PaymentRequestedInfo"] = None
