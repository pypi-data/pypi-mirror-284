from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaInvoice(BaseModel):
    """
    types.MessageMediaInvoice
    ID: 0xf6a548d3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaInvoice'] = pydantic.Field(
        'types.MessageMediaInvoice',
        alias='_'
    )

    title: str
    description: str
    currency: str
    total_amount: int
    start_param: str
    shipping_address_requested: typing.Optional[bool] = None
    test: typing.Optional[bool] = None
    photo: typing.Optional["base.WebDocument"] = None
    receipt_msg_id: typing.Optional[int] = None
    extended_media: typing.Optional["base.MessageExtendedMedia"] = None
