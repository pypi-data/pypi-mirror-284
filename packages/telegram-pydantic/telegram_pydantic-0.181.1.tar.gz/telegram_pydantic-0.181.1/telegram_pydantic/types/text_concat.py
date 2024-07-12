from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextConcat(BaseModel):
    """
    types.TextConcat
    ID: 0x7e6260d7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextConcat'] = pydantic.Field(
        'types.TextConcat',
        alias='_'
    )

    texts: list["base.RichText"]
