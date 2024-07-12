from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetNearestDc(BaseModel):
    """
    functions.help.GetNearestDc
    ID: 0x1fb33026
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetNearestDc'] = pydantic.Field(
        'functions.help.GetNearestDc',
        alias='_'
    )

