from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageListItemText(BaseModel):
    """
    types.PageListItemText
    ID: 0xb92fb6cd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageListItemText'] = pydantic.Field(
        'types.PageListItemText',
        alias='_'
    )

    text: "base.RichText"
