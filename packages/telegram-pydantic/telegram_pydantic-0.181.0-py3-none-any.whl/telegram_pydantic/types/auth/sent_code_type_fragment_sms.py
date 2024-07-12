from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeFragmentSms(BaseModel):
    """
    types.auth.SentCodeTypeFragmentSms
    ID: 0xd9565c39
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeFragmentSms'] = pydantic.Field(
        'types.auth.SentCodeTypeFragmentSms',
        alias='_'
    )

    url: str
    length: int
