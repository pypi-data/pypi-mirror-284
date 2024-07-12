from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputWallPaper(BaseModel):
    """
    types.InputWallPaper
    ID: 0xe630b979
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputWallPaper'] = pydantic.Field(
        'types.InputWallPaper',
        alias='_'
    )

    id: int
    access_hash: int
