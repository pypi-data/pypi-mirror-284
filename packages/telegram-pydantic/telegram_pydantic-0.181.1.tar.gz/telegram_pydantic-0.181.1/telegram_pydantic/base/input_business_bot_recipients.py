from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputBusinessBotRecipients - Layer 181
InputBusinessBotRecipients = typing.Annotated[
    typing.Union[
        types.InputBusinessBotRecipients
    ],
    pydantic.Field(discriminator='QUALNAME')
]
