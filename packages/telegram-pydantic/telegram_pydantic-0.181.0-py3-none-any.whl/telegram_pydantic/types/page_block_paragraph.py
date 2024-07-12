from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockParagraph(BaseModel):
    """
    types.PageBlockParagraph
    ID: 0x467a0766
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockParagraph'] = pydantic.Field(
        'types.PageBlockParagraph',
        alias='_'
    )

    text: "base.RichText"
