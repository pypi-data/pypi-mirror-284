from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallDiscardReasonMissed(BaseModel):
    """
    types.PhoneCallDiscardReasonMissed
    ID: 0x85e42301
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallDiscardReasonMissed'] = pydantic.Field(
        'types.PhoneCallDiscardReasonMissed',
        alias='_'
    )

