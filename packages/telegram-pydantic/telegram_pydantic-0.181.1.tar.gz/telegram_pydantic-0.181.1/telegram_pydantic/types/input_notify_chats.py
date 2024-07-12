from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputNotifyChats(BaseModel):
    """
    types.InputNotifyChats
    ID: 0x4a95e84e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputNotifyChats'] = pydantic.Field(
        'types.InputNotifyChats',
        alias='_'
    )

