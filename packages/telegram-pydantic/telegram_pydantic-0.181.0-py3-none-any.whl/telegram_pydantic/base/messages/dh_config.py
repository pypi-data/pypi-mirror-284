from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.DhConfig - Layer 181
DhConfig = typing.Annotated[
    typing.Union[
        types.messages.DhConfig,
        types.messages.DhConfigNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
