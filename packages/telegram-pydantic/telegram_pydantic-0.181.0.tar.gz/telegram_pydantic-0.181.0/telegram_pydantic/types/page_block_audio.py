from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockAudio(BaseModel):
    """
    types.PageBlockAudio
    ID: 0x804361ea
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockAudio'] = pydantic.Field(
        'types.PageBlockAudio',
        alias='_'
    )

    audio_id: int
    caption: "base.PageCaption"
