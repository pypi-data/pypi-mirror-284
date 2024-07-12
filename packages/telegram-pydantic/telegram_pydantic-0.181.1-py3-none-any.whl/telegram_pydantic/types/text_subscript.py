from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextSubscript(BaseModel):
    """
    types.TextSubscript
    ID: 0xed6a8504
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextSubscript'] = pydantic.Field(
        'types.TextSubscript',
        alias='_'
    )

    text: "base.RichText"
