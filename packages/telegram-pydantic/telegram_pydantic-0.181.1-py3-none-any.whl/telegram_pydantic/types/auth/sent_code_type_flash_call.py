from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeFlashCall(BaseModel):
    """
    types.auth.SentCodeTypeFlashCall
    ID: 0xab03c6d9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeFlashCall'] = pydantic.Field(
        'types.auth.SentCodeTypeFlashCall',
        alias='_'
    )

    pattern: str
