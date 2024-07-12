from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleForum(BaseModel):
    """
    functions.channels.ToggleForum
    ID: 0xa4298b29
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleForum'] = pydantic.Field(
        'functions.channels.ToggleForum',
        alias='_'
    )

    channel: "base.InputChannel"
    enabled: bool
