from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.MessageEditData - Layer 181
MessageEditData = typing.Annotated[
    typing.Union[
        types.messages.MessageEditData
    ],
    pydantic.Field(discriminator='QUALNAME')
]
