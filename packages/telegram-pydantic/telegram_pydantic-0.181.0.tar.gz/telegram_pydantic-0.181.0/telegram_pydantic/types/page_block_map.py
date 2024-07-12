from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockMap(BaseModel):
    """
    types.PageBlockMap
    ID: 0xa44f3ef6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockMap'] = pydantic.Field(
        'types.PageBlockMap',
        alias='_'
    )

    geo: "base.GeoPoint"
    zoom: int
    w: int
    h: int
    caption: "base.PageCaption"
