from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BusinessGreetingMessage - Layer 181
BusinessGreetingMessage = typing.Annotated[
    typing.Union[
        types.BusinessGreetingMessage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
