from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveWallPaper(BaseModel):
    """
    functions.account.SaveWallPaper
    ID: 0x6c5a5b37
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SaveWallPaper'] = pydantic.Field(
        'functions.account.SaveWallPaper',
        alias='_'
    )

    wallpaper: "base.InputWallPaper"
    unsave: bool
    settings: "base.WallPaperSettings"
