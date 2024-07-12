from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Page - Layer 181
Page = typing.Annotated[
    typing.Union[
        types.Page
    ],
    pydantic.Field(discriminator='QUALNAME')
]
