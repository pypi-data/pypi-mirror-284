from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetWallPapers(BaseModel):
    """
    functions.account.GetWallPapers
    ID: 0x7967d36
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetWallPapers'] = pydantic.Field(
        'functions.account.GetWallPapers',
        alias='_'
    )

    hash: int
