from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ValidatedRequestedInfo(BaseModel):
    """
    types.payments.ValidatedRequestedInfo
    ID: 0xd1451883
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.ValidatedRequestedInfo'] = pydantic.Field(
        'types.payments.ValidatedRequestedInfo',
        alias='_'
    )

    id: typing.Optional[str] = None
    shipping_options: typing.Optional[list["base.ShippingOption"]] = None
