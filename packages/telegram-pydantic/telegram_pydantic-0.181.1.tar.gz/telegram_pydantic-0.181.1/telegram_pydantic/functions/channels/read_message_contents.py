from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadMessageContents(BaseModel):
    """
    functions.channels.ReadMessageContents
    ID: 0xeab5dc38
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ReadMessageContents'] = pydantic.Field(
        'functions.channels.ReadMessageContents',
        alias='_'
    )

    channel: "base.InputChannel"
    id: list[int]
