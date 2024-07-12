from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BaseThemeNight(BaseModel):
    """
    types.BaseThemeNight
    ID: 0xb7b31ea8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BaseThemeNight'] = pydantic.Field(
        'types.BaseThemeNight',
        alias='_'
    )

