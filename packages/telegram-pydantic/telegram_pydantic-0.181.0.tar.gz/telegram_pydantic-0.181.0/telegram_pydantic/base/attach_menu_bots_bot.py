from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# AttachMenuBotsBot - Layer 181
AttachMenuBotsBot = typing.Annotated[
    typing.Union[
        types.AttachMenuBotsBot
    ],
    pydantic.Field(discriminator='QUALNAME')
]
