from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextUnderline(BaseModel):
    """
    types.TextUnderline
    ID: 0xc12622c4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextUnderline'] = pydantic.Field(
        'types.TextUnderline',
        alias='_'
    )

    text: "base.RichText"
