from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BaseThemeArctic(BaseModel):
    """
    types.BaseThemeArctic
    ID: 0x5b11125a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BaseThemeArctic'] = pydantic.Field(
        'types.BaseThemeArctic',
        alias='_'
    )

