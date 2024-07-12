from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeFirebaseSms(BaseModel):
    """
    types.auth.SentCodeTypeFirebaseSms
    ID: 0x13c90f17
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeFirebaseSms'] = pydantic.Field(
        'types.auth.SentCodeTypeFirebaseSms',
        alias='_'
    )

    length: int
    nonce: typing.Optional[bytes] = None
    play_integrity_nonce: typing.Optional[bytes] = None
    receipt: typing.Optional[str] = None
    push_timeout: typing.Optional[int] = None
