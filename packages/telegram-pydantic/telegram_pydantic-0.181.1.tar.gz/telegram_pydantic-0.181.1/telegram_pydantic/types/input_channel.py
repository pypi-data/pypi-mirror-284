from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputChannel(BaseModel):
    """
    types.InputChannel
    ID: 0xf35aec28
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputChannel'] = pydantic.Field(
        'types.InputChannel',
        alias='_'
    )

    channel_id: int
    access_hash: int
