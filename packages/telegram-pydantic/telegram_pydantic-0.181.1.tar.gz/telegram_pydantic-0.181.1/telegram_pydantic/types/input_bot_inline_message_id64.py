from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotInlineMessageID64(BaseModel):
    """
    types.InputBotInlineMessageID64
    ID: 0xb6d915d7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotInlineMessageID64'] = pydantic.Field(
        'types.InputBotInlineMessageID64',
        alias='_'
    )

    dc_id: int
    owner_id: int
    id: int
    access_hash: int
