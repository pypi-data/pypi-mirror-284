from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockBlockquote(BaseModel):
    """
    types.PageBlockBlockquote
    ID: 0x263d7c26
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockBlockquote'] = pydantic.Field(
        'types.PageBlockBlockquote',
        alias='_'
    )

    text: "base.RichText"
    caption: "base.RichText"
