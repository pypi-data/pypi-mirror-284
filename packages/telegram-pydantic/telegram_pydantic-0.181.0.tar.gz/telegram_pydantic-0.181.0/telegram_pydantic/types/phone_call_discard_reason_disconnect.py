from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallDiscardReasonDisconnect(BaseModel):
    """
    types.PhoneCallDiscardReasonDisconnect
    ID: 0xe095c1a0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallDiscardReasonDisconnect'] = pydantic.Field(
        'types.PhoneCallDiscardReasonDisconnect',
        alias='_'
    )

