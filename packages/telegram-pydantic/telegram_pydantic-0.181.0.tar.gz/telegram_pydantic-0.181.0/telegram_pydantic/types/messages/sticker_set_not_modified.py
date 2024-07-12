from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerSetNotModified(BaseModel):
    """
    types.messages.StickerSetNotModified
    ID: 0xd3f924eb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.StickerSetNotModified'] = pydantic.Field(
        'types.messages.StickerSetNotModified',
        alias='_'
    )

