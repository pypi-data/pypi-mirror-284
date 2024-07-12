from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadFeaturedStickers(BaseModel):
    """
    types.UpdateReadFeaturedStickers
    ID: 0x571d2742
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadFeaturedStickers'] = pydantic.Field(
        'types.UpdateReadFeaturedStickers',
        alias='_'
    )

