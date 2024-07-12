from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TranscribedAudio(BaseModel):
    """
    types.messages.TranscribedAudio
    ID: 0xcfb9d957
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.TranscribedAudio'] = pydantic.Field(
        'types.messages.TranscribedAudio',
        alias='_'
    )

    transcription_id: int
    text: str
    pending: typing.Optional[bool] = None
    trial_remains_num: typing.Optional[int] = None
    trial_remains_until_date: typing.Optional[int] = None
