from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockFooter(BaseModel):
    """
    types.PageBlockFooter
    ID: 0x48870999
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockFooter'] = pydantic.Field(
        'types.PageBlockFooter',
        alias='_'
    )

    text: "base.RichText"
