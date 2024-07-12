from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Photo - Layer 181
Photo = typing.Annotated[
    typing.Union[
        types.Photo,
        types.PhotoEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
