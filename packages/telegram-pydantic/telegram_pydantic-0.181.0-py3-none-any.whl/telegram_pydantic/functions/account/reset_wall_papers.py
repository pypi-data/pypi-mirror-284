from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetWallPapers(BaseModel):
    """
    functions.account.ResetWallPapers
    ID: 0xbb3b9804
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ResetWallPapers'] = pydantic.Field(
        'functions.account.ResetWallPapers',
        alias='_'
    )

