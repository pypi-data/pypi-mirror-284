from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Username - Layer 181
Username = typing.Annotated[
    typing.Union[
        types.Username
    ],
    pydantic.Field(discriminator='QUALNAME')
]
