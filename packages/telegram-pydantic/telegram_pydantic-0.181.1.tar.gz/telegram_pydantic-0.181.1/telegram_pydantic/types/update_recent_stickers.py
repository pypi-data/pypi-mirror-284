from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateRecentStickers(BaseModel):
    """
    types.UpdateRecentStickers
    ID: 0x9a422c20
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateRecentStickers'] = pydantic.Field(
        'types.UpdateRecentStickers',
        alias='_'
    )

