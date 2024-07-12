from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# KeyboardButtonRow - Layer 181
KeyboardButtonRow = typing.Annotated[
    typing.Union[
        types.KeyboardButtonRow
    ],
    pydantic.Field(discriminator='QUALNAME')
]
