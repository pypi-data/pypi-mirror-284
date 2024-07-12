from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# WebPageAttribute - Layer 181
WebPageAttribute = typing.Annotated[
    typing.Union[
        types.WebPageAttributeStickerSet,
        types.WebPageAttributeStory,
        types.WebPageAttributeTheme
    ],
    pydantic.Field(discriminator='QUALNAME')
]
