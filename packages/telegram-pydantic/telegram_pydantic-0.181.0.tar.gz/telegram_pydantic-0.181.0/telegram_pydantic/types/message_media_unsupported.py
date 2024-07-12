from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaUnsupported(BaseModel):
    """
    types.MessageMediaUnsupported
    ID: 0x9f84f49e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaUnsupported'] = pydantic.Field(
        'types.MessageMediaUnsupported',
        alias='_'
    )

