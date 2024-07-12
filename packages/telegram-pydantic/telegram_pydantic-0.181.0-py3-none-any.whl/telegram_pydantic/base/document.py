from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Document - Layer 181
Document = typing.Annotated[
    typing.Union[
        types.Document,
        types.DocumentEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
