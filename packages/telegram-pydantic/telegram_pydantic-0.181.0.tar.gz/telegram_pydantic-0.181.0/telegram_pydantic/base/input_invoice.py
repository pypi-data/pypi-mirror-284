from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputInvoice - Layer 181
InputInvoice = typing.Annotated[
    typing.Union[
        types.InputInvoiceMessage,
        types.InputInvoicePremiumGiftCode,
        types.InputInvoiceSlug,
        types.InputInvoiceStars
    ],
    pydantic.Field(discriminator='QUALNAME')
]
