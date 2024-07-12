from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageUploadAudioAction(BaseModel):
    """
    types.SendMessageUploadAudioAction
    ID: 0xf351d7ab
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageUploadAudioAction'] = pydantic.Field(
        'types.SendMessageUploadAudioAction',
        alias='_'
    )

    progress: int
