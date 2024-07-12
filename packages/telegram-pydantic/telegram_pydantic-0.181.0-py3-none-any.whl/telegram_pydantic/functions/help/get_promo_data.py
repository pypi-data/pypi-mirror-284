from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPromoData(BaseModel):
    """
    functions.help.GetPromoData
    ID: 0xc0977421
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetPromoData'] = pydantic.Field(
        'functions.help.GetPromoData',
        alias='_'
    )

