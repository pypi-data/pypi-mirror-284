from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCode(BaseModel):
    """
    types.auth.SentCode
    ID: 0x5e002502
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCode'] = pydantic.Field(
        'types.auth.SentCode',
        alias='_'
    )

    type: "base.auth.SentCodeType"
    phone_code_hash: str
    next_type: typing.Optional["base.auth.CodeType"] = None
    timeout: typing.Optional[int] = None
