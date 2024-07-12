from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextMarked(BaseModel):
    """
    types.TextMarked
    ID: 0x34b8621
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextMarked'] = pydantic.Field(
        'types.TextMarked',
        alias='_'
    )

    text: "base.RichText"
