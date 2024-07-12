from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AutoSaveSettings(BaseModel):
    """
    types.AutoSaveSettings
    ID: 0xc84834ce
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AutoSaveSettings'] = pydantic.Field(
        'types.AutoSaveSettings',
        alias='_'
    )

    photos: typing.Optional[bool] = None
    videos: typing.Optional[bool] = None
    video_max_size: typing.Optional[int] = None
