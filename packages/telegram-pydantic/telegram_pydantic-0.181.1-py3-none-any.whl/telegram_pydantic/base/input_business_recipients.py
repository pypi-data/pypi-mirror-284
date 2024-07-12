from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputBusinessRecipients - Layer 181
InputBusinessRecipients = typing.Annotated[
    typing.Union[
        types.InputBusinessRecipients
    ],
    pydantic.Field(discriminator='QUALNAME')
]
