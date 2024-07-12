from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageListOrderedItemText(BaseModel):
    """
    types.PageListOrderedItemText
    ID: 0x5e068047
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageListOrderedItemText'] = pydantic.Field(
        'types.PageListOrderedItemText',
        alias='_'
    )

    num: str
    text: "base.RichText"
