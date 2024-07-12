from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChatOnlines - Layer 181
ChatOnlines = typing.Annotated[
    typing.Union[
        types.ChatOnlines
    ],
    pydantic.Field(discriminator='QUALNAME')
]
