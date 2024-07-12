from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportInvoice(BaseModel):
    """
    functions.payments.ExportInvoice
    ID: 0xf91b065
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.ExportInvoice'] = pydantic.Field(
        'functions.payments.ExportInvoice',
        alias='_'
    )

    invoice_media: "base.InputMedia"
