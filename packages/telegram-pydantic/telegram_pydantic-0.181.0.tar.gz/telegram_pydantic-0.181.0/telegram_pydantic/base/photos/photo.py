from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# photos.Photo - Layer 181
Photo = typing.Annotated[
    typing.Union[
        types.photos.Photo
    ],
    pydantic.Field(discriminator='QUALNAME')
]
