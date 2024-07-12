from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DocumentAttributeAudio(BaseModel):
    """
    types.DocumentAttributeAudio
    ID: 0x9852f9c6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DocumentAttributeAudio'] = pydantic.Field(
        'types.DocumentAttributeAudio',
        alias='_'
    )

    duration: int
    voice: typing.Optional[bool] = None
    title: typing.Optional[str] = None
    performer: typing.Optional[str] = None
    waveform: typing.Optional[bytes] = None
