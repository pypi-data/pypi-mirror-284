from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.InactiveChats - Layer 181
InactiveChats = typing.Annotated[
    typing.Union[
        types.messages.InactiveChats
    ],
    pydantic.Field(discriminator='QUALNAME')
]
