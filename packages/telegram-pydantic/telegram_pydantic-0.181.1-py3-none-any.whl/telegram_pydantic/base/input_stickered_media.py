from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputStickeredMedia - Layer 181
InputStickeredMedia = typing.Annotated[
    typing.Union[
        types.InputStickeredMediaDocument,
        types.InputStickeredMediaPhoto
    ],
    pydantic.Field(discriminator='QUALNAME')
]
