from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditPhoto(BaseModel):
    """
    functions.channels.EditPhoto
    ID: 0xf12e57c9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.EditPhoto'] = pydantic.Field(
        'functions.channels.EditPhoto',
        alias='_'
    )

    channel: "base.InputChannel"
    photo: "base.InputChatPhoto"
