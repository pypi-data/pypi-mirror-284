from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WallPapers(BaseModel):
    """
    types.account.WallPapers
    ID: 0xcdc3858c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.WallPapers'] = pydantic.Field(
        'types.account.WallPapers',
        alias='_'
    )

    hash: int
    wallpapers: list["base.WallPaper"]
