from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MessageExtendedMedia - Layer 181
MessageExtendedMedia = typing.Annotated[
    typing.Union[
        types.MessageExtendedMedia,
        types.MessageExtendedMediaPreview
    ],
    pydantic.Field(discriminator='QUALNAME')
]
