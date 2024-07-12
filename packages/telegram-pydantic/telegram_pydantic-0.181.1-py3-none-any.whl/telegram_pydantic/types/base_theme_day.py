from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BaseThemeDay(BaseModel):
    """
    types.BaseThemeDay
    ID: 0xfbd81688
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BaseThemeDay'] = pydantic.Field(
        'types.BaseThemeDay',
        alias='_'
    )

