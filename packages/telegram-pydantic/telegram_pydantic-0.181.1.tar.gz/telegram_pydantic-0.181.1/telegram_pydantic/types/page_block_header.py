from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockHeader(BaseModel):
    """
    types.PageBlockHeader
    ID: 0xbfd064ec
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockHeader'] = pydantic.Field(
        'types.PageBlockHeader',
        alias='_'
    )

    text: "base.RichText"
