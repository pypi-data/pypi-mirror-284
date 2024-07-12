from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedInvoice(BaseModel):
    """
    types.payments.ExportedInvoice
    ID: 0xaed0cbd9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.ExportedInvoice'] = pydantic.Field(
        'types.payments.ExportedInvoice',
        alias='_'
    )

    url: str
