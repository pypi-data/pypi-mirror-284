from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateFavedStickers(BaseModel):
    """
    types.UpdateFavedStickers
    ID: 0xe511996d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateFavedStickers'] = pydantic.Field(
        'types.UpdateFavedStickers',
        alias='_'
    )

