from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallDiscarded(BaseModel):
    """
    types.PhoneCallDiscarded
    ID: 0x50ca4de1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallDiscarded'] = pydantic.Field(
        'types.PhoneCallDiscarded',
        alias='_'
    )

    id: int
    need_rating: typing.Optional[bool] = None
    need_debug: typing.Optional[bool] = None
    video: typing.Optional[bool] = None
    reason: typing.Optional["base.PhoneCallDiscardReason"] = None
    duration: typing.Optional[int] = None
