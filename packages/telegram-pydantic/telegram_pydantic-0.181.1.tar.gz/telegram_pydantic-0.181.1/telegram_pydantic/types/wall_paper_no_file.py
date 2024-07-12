from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WallPaperNoFile(BaseModel):
    """
    types.WallPaperNoFile
    ID: 0xe0804116
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WallPaperNoFile'] = pydantic.Field(
        'types.WallPaperNoFile',
        alias='_'
    )

    id: int
    default: typing.Optional[bool] = None
    dark: typing.Optional[bool] = None
    settings: typing.Optional["base.WallPaperSettings"] = None
