from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.DialogFilters - Layer 181
DialogFilters = typing.Annotated[
    typing.Union[
        types.messages.DialogFilters
    ],
    pydantic.Field(discriminator='QUALNAME')
]
