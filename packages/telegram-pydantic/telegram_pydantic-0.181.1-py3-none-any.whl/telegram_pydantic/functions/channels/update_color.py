from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateColor(BaseModel):
    """
    functions.channels.UpdateColor
    ID: 0xd8aa3671
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.UpdateColor'] = pydantic.Field(
        'functions.channels.UpdateColor',
        alias='_'
    )

    channel: "base.InputChannel"
    for_profile: typing.Optional[bool] = None
    color: typing.Optional[int] = None
    background_emoji_id: typing.Optional[int] = None
