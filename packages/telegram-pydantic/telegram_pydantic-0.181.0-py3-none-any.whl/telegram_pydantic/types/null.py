from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Null(BaseModel):
    """
    types.Null
    ID: 0x56730bcc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Null'] = pydantic.Field(
        'types.Null',
        alias='_'
    )

