from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerSetInstallResultSuccess(BaseModel):
    """
    types.messages.StickerSetInstallResultSuccess
    ID: 0x38641628
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.StickerSetInstallResultSuccess'] = pydantic.Field(
        'types.messages.StickerSetInstallResultSuccess',
        alias='_'
    )

