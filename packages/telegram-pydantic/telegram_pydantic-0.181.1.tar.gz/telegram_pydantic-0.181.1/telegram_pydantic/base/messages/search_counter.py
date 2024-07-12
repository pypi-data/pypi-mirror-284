from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.SearchCounter - Layer 181
SearchCounter = typing.Annotated[
    typing.Union[
        types.messages.SearchCounter
    ],
    pydantic.Field(discriminator='QUALNAME')
]
