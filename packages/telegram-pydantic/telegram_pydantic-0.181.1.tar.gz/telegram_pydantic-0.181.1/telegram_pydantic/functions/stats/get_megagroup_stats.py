from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMegagroupStats(BaseModel):
    """
    functions.stats.GetMegagroupStats
    ID: 0xdcdf8607
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetMegagroupStats'] = pydantic.Field(
        'functions.stats.GetMegagroupStats',
        alias='_'
    )

    channel: "base.InputChannel"
    dark: typing.Optional[bool] = None
