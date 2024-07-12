from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputAppEvent - Layer 181
InputAppEvent = typing.Annotated[
    typing.Union[
        types.InputAppEvent
    ],
    pydantic.Field(discriminator='QUALNAME')
]
