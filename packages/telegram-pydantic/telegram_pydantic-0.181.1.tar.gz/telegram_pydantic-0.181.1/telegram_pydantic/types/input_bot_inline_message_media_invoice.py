from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotInlineMessageMediaInvoice(BaseModel):
    """
    types.InputBotInlineMessageMediaInvoice
    ID: 0xd7e78225
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotInlineMessageMediaInvoice'] = pydantic.Field(
        'types.InputBotInlineMessageMediaInvoice',
        alias='_'
    )

    title: str
    description: str
    invoice: "base.Invoice"
    payload: bytes
    provider: str
    provider_data: "base.DataJSON"
    photo: typing.Optional["base.InputWebDocument"] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
