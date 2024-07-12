from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputWallPaperNoFile(BaseModel):
    """
    types.InputWallPaperNoFile
    ID: 0x967a462e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputWallPaperNoFile'] = pydantic.Field(
        'types.InputWallPaperNoFile',
        alias='_'
    )

    id: int
