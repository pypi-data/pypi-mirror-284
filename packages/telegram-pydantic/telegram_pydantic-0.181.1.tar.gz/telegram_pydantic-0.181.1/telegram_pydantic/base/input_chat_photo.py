from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputChatPhoto - Layer 181
InputChatPhoto = typing.Annotated[
    typing.Union[
        types.InputChatPhoto,
        types.InputChatPhotoEmpty,
        types.InputChatUploadedPhoto
    ],
    pydantic.Field(discriminator='QUALNAME')
]
