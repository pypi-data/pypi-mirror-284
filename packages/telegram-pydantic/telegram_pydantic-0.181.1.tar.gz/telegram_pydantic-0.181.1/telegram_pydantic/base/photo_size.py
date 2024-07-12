from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PhotoSize - Layer 181
PhotoSize = typing.Annotated[
    typing.Union[
        types.PhotoCachedSize,
        types.PhotoPathSize,
        types.PhotoSize,
        types.PhotoSizeEmpty,
        types.PhotoSizeProgressive,
        types.PhotoStrippedSize
    ],
    pydantic.Field(discriminator='QUALNAME')
]
