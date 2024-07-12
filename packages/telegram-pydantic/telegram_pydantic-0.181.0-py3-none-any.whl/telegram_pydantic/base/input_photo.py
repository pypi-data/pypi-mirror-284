from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputPhoto - Layer 181
InputPhoto = typing.Annotated[
    typing.Union[
        types.InputPhoto,
        types.InputPhotoEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
