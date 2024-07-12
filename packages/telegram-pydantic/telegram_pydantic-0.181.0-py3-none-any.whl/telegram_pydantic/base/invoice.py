from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Invoice - Layer 181
Invoice = typing.Annotated[
    typing.Union[
        types.Invoice
    ],
    pydantic.Field(discriminator='QUALNAME')
]
