from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# photos.Photos - Layer 181
Photos = typing.Annotated[
    typing.Union[
        types.photos.Photos,
        types.photos.PhotosSlice
    ],
    pydantic.Field(discriminator='QUALNAME')
]
