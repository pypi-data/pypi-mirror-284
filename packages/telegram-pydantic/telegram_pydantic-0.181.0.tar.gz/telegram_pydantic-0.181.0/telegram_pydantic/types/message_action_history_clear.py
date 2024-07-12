from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionHistoryClear(BaseModel):
    """
    types.MessageActionHistoryClear
    ID: 0x9fbab604
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionHistoryClear'] = pydantic.Field(
        'types.MessageActionHistoryClear',
        alias='_'
    )

