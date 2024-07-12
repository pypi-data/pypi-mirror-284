from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerSetInstallResultArchive(BaseModel):
    """
    types.messages.StickerSetInstallResultArchive
    ID: 0x35e410a8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.StickerSetInstallResultArchive'] = pydantic.Field(
        'types.messages.StickerSetInstallResultArchive',
        alias='_'
    )

    sets: list["base.StickerSetCovered"]
