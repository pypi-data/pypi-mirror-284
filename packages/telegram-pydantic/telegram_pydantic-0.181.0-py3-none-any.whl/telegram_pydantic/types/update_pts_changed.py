from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePtsChanged(BaseModel):
    """
    types.UpdatePtsChanged
    ID: 0x3354678f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePtsChanged'] = pydantic.Field(
        'types.UpdatePtsChanged',
        alias='_'
    )

