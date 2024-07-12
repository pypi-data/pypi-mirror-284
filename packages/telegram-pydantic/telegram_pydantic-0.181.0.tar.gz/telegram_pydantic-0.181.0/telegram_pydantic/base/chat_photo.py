from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChatPhoto - Layer 181
ChatPhoto = typing.Annotated[
    typing.Union[
        types.ChatPhoto,
        types.ChatPhotoEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
