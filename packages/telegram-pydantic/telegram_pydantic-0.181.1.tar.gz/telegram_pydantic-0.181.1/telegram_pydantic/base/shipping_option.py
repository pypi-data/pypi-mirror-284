from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ShippingOption - Layer 181
ShippingOption = typing.Annotated[
    typing.Union[
        types.ShippingOption
    ],
    pydantic.Field(discriminator='QUALNAME')
]
