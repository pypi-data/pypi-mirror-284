from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.CountryCode - Layer 181
CountryCode = typing.Annotated[
    typing.Union[
        types.help.CountryCode
    ],
    pydantic.Field(discriminator='QUALNAME')
]
