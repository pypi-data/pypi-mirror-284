from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PostAddress - Layer 181
PostAddress = typing.Annotated[
    typing.Union[
        types.PostAddress
    ],
    pydantic.Field(discriminator='QUALNAME')
]
