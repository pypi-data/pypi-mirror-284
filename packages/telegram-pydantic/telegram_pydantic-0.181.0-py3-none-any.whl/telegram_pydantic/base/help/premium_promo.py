from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.PremiumPromo - Layer 181
PremiumPromo = typing.Annotated[
    typing.Union[
        types.help.PremiumPromo
    ],
    pydantic.Field(discriminator='QUALNAME')
]
