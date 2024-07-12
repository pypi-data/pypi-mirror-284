from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# UserProfilePhoto - Layer 181
UserProfilePhoto = typing.Annotated[
    typing.Union[
        types.UserProfilePhoto,
        types.UserProfilePhotoEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
