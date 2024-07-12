from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotInlineMessageID(BaseModel):
    """
    types.InputBotInlineMessageID
    ID: 0x890c3d89
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotInlineMessageID'] = pydantic.Field(
        'types.InputBotInlineMessageID',
        alias='_'
    )

    dc_id: int
    id: int
    access_hash: int
