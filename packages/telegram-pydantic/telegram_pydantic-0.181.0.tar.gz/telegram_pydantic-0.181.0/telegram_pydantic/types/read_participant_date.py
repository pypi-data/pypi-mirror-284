from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadParticipantDate(BaseModel):
    """
    types.ReadParticipantDate
    ID: 0x4a4ff172
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReadParticipantDate'] = pydantic.Field(
        'types.ReadParticipantDate',
        alias='_'
    )

    user_id: int
    date: int
