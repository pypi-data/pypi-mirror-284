from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputWebDocument - Layer 181
InputWebDocument = typing.Annotated[
    typing.Union[
        types.InputWebDocument
    ],
    pydantic.Field(discriminator='QUALNAME')
]
