from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputGroupCallStream(BaseModel):
    """
    types.InputGroupCallStream
    ID: 0x598a92a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputGroupCallStream'] = pydantic.Field(
        'types.InputGroupCallStream',
        alias='_'
    )

    call: "base.InputGroupCall"
    time_ms: int
    scale: int
    video_channel: typing.Optional[int] = None
    video_quality: typing.Optional[int] = None
