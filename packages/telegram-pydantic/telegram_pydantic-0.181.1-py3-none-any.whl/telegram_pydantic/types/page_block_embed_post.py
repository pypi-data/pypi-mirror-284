from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockEmbedPost(BaseModel):
    """
    types.PageBlockEmbedPost
    ID: 0xf259a80b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockEmbedPost'] = pydantic.Field(
        'types.PageBlockEmbedPost',
        alias='_'
    )

    url: str
    webpage_id: int
    author_photo_id: int
    author: str
    date: int
    blocks: list["base.PageBlock"]
    caption: "base.PageCaption"
