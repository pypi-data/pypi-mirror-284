from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FoundStickerSetsNotModified(BaseModel):
    """
    types.messages.FoundStickerSetsNotModified
    ID: 0xd54b65d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.FoundStickerSetsNotModified'] = pydantic.Field(
        'types.messages.FoundStickerSetsNotModified',
        alias='_'
    )

