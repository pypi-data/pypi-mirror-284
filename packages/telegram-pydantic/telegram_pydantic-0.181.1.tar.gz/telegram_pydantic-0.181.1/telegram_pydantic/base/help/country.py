from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.Country - Layer 181
Country = typing.Annotated[
    typing.Union[
        types.help.Country
    ],
    pydantic.Field(discriminator='QUALNAME')
]
