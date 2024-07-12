from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageCaption(BaseModel):
    """
    types.PageCaption
    ID: 0x6f747657
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageCaption'] = pydantic.Field(
        'types.PageCaption',
        alias='_'
    )

    text: "base.RichText"
    credit: "base.RichText"
