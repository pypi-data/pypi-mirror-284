from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Theme - Layer 181
Theme = typing.Annotated[
    typing.Union[
        types.Theme
    ],
    pydantic.Field(discriminator='QUALNAME')
]
