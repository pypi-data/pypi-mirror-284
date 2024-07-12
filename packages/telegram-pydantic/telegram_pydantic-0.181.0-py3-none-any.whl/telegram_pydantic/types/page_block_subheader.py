from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockSubheader(BaseModel):
    """
    types.PageBlockSubheader
    ID: 0xf12bb6e1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockSubheader'] = pydantic.Field(
        'types.PageBlockSubheader',
        alias='_'
    )

    text: "base.RichText"
