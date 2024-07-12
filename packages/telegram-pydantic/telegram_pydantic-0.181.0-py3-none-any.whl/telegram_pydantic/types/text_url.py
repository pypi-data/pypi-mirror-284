from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextUrl(BaseModel):
    """
    types.TextUrl
    ID: 0x3c2884c1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextUrl'] = pydantic.Field(
        'types.TextUrl',
        alias='_'
    )

    text: "base.RichText"
    url: str
    webpage_id: int
