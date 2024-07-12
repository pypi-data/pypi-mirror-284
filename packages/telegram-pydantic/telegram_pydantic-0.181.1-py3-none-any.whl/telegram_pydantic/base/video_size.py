from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# VideoSize - Layer 181
VideoSize = typing.Annotated[
    typing.Union[
        types.VideoSize,
        types.VideoSizeEmojiMarkup,
        types.VideoSizeStickerMarkup
    ],
    pydantic.Field(discriminator='QUALNAME')
]
