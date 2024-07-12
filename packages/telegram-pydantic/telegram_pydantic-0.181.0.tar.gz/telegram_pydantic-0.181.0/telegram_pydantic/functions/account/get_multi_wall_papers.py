from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMultiWallPapers(BaseModel):
    """
    functions.account.GetMultiWallPapers
    ID: 0x65ad71dc
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetMultiWallPapers'] = pydantic.Field(
        'functions.account.GetMultiWallPapers',
        alias='_'
    )

    wallpapers: list["base.InputWallPaper"]
