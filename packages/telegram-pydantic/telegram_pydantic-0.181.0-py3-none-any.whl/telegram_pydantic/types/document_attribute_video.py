from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DocumentAttributeVideo(BaseModel):
    """
    types.DocumentAttributeVideo
    ID: 0xd38ff1c2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DocumentAttributeVideo'] = pydantic.Field(
        'types.DocumentAttributeVideo',
        alias='_'
    )

    duration: float
    w: int
    h: int
    round_message: typing.Optional[bool] = None
    supports_streaming: typing.Optional[bool] = None
    nosound: typing.Optional[bool] = None
    preload_prefix_size: typing.Optional[int] = None
