from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Message - Layer 181
Message = typing.Annotated[
    typing.Union[
        types.Message,
        types.MessageEmpty,
        types.MessageService
    ],
    pydantic.Field(discriminator='QUALNAME')
]
