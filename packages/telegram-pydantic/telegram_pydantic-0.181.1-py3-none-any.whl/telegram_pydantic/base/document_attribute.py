from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# DocumentAttribute - Layer 181
DocumentAttribute = typing.Annotated[
    typing.Union[
        types.DocumentAttributeAnimated,
        types.DocumentAttributeAudio,
        types.DocumentAttributeCustomEmoji,
        types.DocumentAttributeFilename,
        types.DocumentAttributeHasStickers,
        types.DocumentAttributeImageSize,
        types.DocumentAttributeSticker,
        types.DocumentAttributeVideo
    ],
    pydantic.Field(discriminator='QUALNAME')
]
