from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaInvoice(BaseModel):
    """
    types.InputMediaInvoice
    ID: 0x405fef0d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaInvoice'] = pydantic.Field(
        'types.InputMediaInvoice',
        alias='_'
    )

    title: str
    description: str
    invoice: "base.Invoice"
    payload: bytes
    provider_data: "base.DataJSON"
    photo: typing.Optional["base.InputWebDocument"] = None
    provider: typing.Optional[str] = None
    start_param: typing.Optional[str] = None
    extended_media: typing.Optional["base.InputMedia"] = None
