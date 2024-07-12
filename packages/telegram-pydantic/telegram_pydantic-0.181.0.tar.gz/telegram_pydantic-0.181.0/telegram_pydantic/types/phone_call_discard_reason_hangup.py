from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallDiscardReasonHangup(BaseModel):
    """
    types.PhoneCallDiscardReasonHangup
    ID: 0x57adc690
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallDiscardReasonHangup'] = pydantic.Field(
        'types.PhoneCallDiscardReasonHangup',
        alias='_'
    )

