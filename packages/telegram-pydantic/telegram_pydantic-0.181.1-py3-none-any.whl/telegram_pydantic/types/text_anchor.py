from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextAnchor(BaseModel):
    """
    types.TextAnchor
    ID: 0x35553762
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextAnchor'] = pydantic.Field(
        'types.TextAnchor',
        alias='_'
    )

    text: "base.RichText"
    name: str
