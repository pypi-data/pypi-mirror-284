from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Poll - Layer 181
Poll = typing.Annotated[
    typing.Union[
        types.Poll
    ],
    pydantic.Field(discriminator='QUALNAME')
]
