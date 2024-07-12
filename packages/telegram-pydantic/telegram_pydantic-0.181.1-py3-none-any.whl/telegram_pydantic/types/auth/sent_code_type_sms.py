from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeSms(BaseModel):
    """
    types.auth.SentCodeTypeSms
    ID: 0xc000bba2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeSms'] = pydantic.Field(
        'types.auth.SentCodeTypeSms',
        alias='_'
    )

    length: int
