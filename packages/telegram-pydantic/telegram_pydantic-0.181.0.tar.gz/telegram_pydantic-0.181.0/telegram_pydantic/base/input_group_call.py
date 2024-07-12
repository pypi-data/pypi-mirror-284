from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputGroupCall - Layer 181
InputGroupCall = typing.Annotated[
    typing.Union[
        types.InputGroupCall
    ],
    pydantic.Field(discriminator='QUALNAME')
]
