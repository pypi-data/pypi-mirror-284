from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextFixed(BaseModel):
    """
    types.TextFixed
    ID: 0x6c3f19b9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextFixed'] = pydantic.Field(
        'types.TextFixed',
        alias='_'
    )

    text: "base.RichText"
