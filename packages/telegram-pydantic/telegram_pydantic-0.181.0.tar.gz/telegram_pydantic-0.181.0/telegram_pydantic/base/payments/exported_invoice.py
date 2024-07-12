from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# payments.ExportedInvoice - Layer 181
ExportedInvoice = typing.Annotated[
    typing.Union[
        types.payments.ExportedInvoice
    ],
    pydantic.Field(discriminator='QUALNAME')
]
