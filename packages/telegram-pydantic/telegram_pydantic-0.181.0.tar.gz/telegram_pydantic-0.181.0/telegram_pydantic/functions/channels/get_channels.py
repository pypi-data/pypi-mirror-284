from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChannels(BaseModel):
    """
    functions.channels.GetChannels
    ID: 0xa7f6bbb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetChannels'] = pydantic.Field(
        'functions.channels.GetChannels',
        alias='_'
    )

    id: list["base.InputChannel"]
