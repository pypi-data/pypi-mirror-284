from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.StickerSetInstallResult - Layer 181
StickerSetInstallResult = typing.Annotated[
    typing.Union[
        types.messages.StickerSetInstallResultArchive,
        types.messages.StickerSetInstallResultSuccess
    ],
    pydantic.Field(discriminator='QUALNAME')
]
