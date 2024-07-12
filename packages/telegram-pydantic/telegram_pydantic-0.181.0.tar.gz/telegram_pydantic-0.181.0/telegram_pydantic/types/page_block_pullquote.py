from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockPullquote(BaseModel):
    """
    types.PageBlockPullquote
    ID: 0x4f4456d3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockPullquote'] = pydantic.Field(
        'types.PageBlockPullquote',
        alias='_'
    )

    text: "base.RichText"
    caption: "base.RichText"
