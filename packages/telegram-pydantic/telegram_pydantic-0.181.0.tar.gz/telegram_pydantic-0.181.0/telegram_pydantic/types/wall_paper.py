from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WallPaper(BaseModel):
    """
    types.WallPaper
    ID: 0xa437c3ed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WallPaper'] = pydantic.Field(
        'types.WallPaper',
        alias='_'
    )

    id: int
    access_hash: int
    slug: str
    document: "base.Document"
    creator: typing.Optional[bool] = None
    default: typing.Optional[bool] = None
    pattern: typing.Optional[bool] = None
    dark: typing.Optional[bool] = None
    settings: typing.Optional["base.WallPaperSettings"] = None
