from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionSetMessagesTTL(BaseModel):
    """
    types.MessageActionSetMessagesTTL
    ID: 0x3c134d7b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionSetMessagesTTL'] = pydantic.Field(
        'types.MessageActionSetMessagesTTL',
        alias='_'
    )

    period: int
    auto_setting_from: typing.Optional[int] = None
