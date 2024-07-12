from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallDiscardReasonBusy(BaseModel):
    """
    types.PhoneCallDiscardReasonBusy
    ID: 0xfaf7e8c9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallDiscardReasonBusy'] = pydantic.Field(
        'types.PhoneCallDiscardReasonBusy',
        alias='_'
    )

