from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextSuperscript(BaseModel):
    """
    types.TextSuperscript
    ID: 0xc7fb5e01
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextSuperscript'] = pydantic.Field(
        'types.TextSuperscript',
        alias='_'
    )

    text: "base.RichText"
