from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BaseThemeClassic(BaseModel):
    """
    types.BaseThemeClassic
    ID: 0xc3a12462
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BaseThemeClassic'] = pydantic.Field(
        'types.BaseThemeClassic',
        alias='_'
    )

