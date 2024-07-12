from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateSavedGifs(BaseModel):
    """
    types.UpdateSavedGifs
    ID: 0x9375341e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateSavedGifs'] = pydantic.Field(
        'types.UpdateSavedGifs',
        alias='_'
    )

