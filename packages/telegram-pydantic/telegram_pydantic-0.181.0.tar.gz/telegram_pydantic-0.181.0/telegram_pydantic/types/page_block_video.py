from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockVideo(BaseModel):
    """
    types.PageBlockVideo
    ID: 0x7c8fe7b6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockVideo'] = pydantic.Field(
        'types.PageBlockVideo',
        alias='_'
    )

    video_id: int
    caption: "base.PageCaption"
    autoplay: typing.Optional[bool] = None
    loop: typing.Optional[bool] = None
