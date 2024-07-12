from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetWallPaper(BaseModel):
    """
    functions.account.GetWallPaper
    ID: 0xfc8ddbea
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetWallPaper'] = pydantic.Field(
        'functions.account.GetWallPaper',
        alias='_'
    )

    wallpaper: "base.InputWallPaper"
