from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockEmbed(BaseModel):
    """
    types.PageBlockEmbed
    ID: 0xa8718dc5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockEmbed'] = pydantic.Field(
        'types.PageBlockEmbed',
        alias='_'
    )

    caption: "base.PageCaption"
    full_width: typing.Optional[bool] = None
    allow_scrolling: typing.Optional[bool] = None
    url: typing.Optional[str] = None
    html: typing.Optional[str] = None
    poster_photo_id: typing.Optional[int] = None
    w: typing.Optional[int] = None
    h: typing.Optional[int] = None
