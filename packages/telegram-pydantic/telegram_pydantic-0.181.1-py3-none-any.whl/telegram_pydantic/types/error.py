from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Error(BaseModel):
    """
    types.Error
    ID: 0xc4b9f9bb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Error'] = pydantic.Field(
        'types.Error',
        alias='_'
    )

    code: int
    text: str
