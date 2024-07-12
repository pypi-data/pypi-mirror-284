from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Config - Layer 181
Config = typing.Annotated[
    typing.Union[
        types.Config
    ],
    pydantic.Field(discriminator='QUALNAME')
]
