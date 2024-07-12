from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionScreenshotTaken(BaseModel):
    """
    types.MessageActionScreenshotTaken
    ID: 0x4792929b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionScreenshotTaken'] = pydantic.Field(
        'types.MessageActionScreenshotTaken',
        alias='_'
    )

