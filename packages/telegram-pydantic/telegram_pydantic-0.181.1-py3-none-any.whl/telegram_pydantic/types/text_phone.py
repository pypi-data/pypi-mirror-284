from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextPhone(BaseModel):
    """
    types.TextPhone
    ID: 0x1ccb966a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextPhone'] = pydantic.Field(
        'types.TextPhone',
        alias='_'
    )

    text: "base.RichText"
    phone: str
