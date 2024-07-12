from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# updates.State - Layer 181
State = typing.Annotated[
    typing.Union[
        types.updates.State
    ],
    pydantic.Field(discriminator='QUALNAME')
]
