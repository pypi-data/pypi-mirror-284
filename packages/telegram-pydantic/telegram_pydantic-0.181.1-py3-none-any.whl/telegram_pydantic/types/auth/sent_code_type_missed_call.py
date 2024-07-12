from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeMissedCall(BaseModel):
    """
    types.auth.SentCodeTypeMissedCall
    ID: 0x82006484
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeMissedCall'] = pydantic.Field(
        'types.auth.SentCodeTypeMissedCall',
        alias='_'
    )

    prefix: str
    length: int
