from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BaseThemeTinted(BaseModel):
    """
    types.BaseThemeTinted
    ID: 0x6d5f77ee
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BaseThemeTinted'] = pydantic.Field(
        'types.BaseThemeTinted',
        alias='_'
    )

