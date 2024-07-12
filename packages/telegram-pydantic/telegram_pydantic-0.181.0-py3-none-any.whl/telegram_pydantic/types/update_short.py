from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateShort(BaseModel):
    """
    types.UpdateShort
    ID: 0x78d4dec1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateShort'] = pydantic.Field(
        'types.UpdateShort',
        alias='_'
    )

    update: "base.Update"
    date: int
