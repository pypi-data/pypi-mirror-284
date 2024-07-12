from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeSmsWord(BaseModel):
    """
    types.auth.SentCodeTypeSmsWord
    ID: 0xa416ac81
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeSmsWord'] = pydantic.Field(
        'types.auth.SentCodeTypeSmsWord',
        alias='_'
    )

    beginning: typing.Optional[str] = None
