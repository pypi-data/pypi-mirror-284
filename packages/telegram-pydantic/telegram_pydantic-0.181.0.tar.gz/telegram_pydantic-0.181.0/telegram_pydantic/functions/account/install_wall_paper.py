from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InstallWallPaper(BaseModel):
    """
    functions.account.InstallWallPaper
    ID: 0xfeed5769
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.InstallWallPaper'] = pydantic.Field(
        'functions.account.InstallWallPaper',
        alias='_'
    )

    wallpaper: "base.InputWallPaper"
    settings: "base.WallPaperSettings"
