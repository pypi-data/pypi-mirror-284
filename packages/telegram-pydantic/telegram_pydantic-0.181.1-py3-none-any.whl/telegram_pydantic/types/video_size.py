from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class VideoSize(BaseModel):
    """
    types.VideoSize
    ID: 0xde33b094
    Layer: 181
    """
    QUALNAME: typing.Literal['types.VideoSize'] = pydantic.Field(
        'types.VideoSize',
        alias='_'
    )

    type: str
    w: int
    h: int
    size: int
    video_start_ts: typing.Optional[float] = None
