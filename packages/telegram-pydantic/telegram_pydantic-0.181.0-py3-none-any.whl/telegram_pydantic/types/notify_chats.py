from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NotifyChats(BaseModel):
    """
    types.NotifyChats
    ID: 0xc007cec3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NotifyChats'] = pydantic.Field(
        'types.NotifyChats',
        alias='_'
    )

