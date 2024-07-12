from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDeleteMessages(BaseModel):
    """
    types.UpdateDeleteMessages
    ID: 0xa20db0e5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDeleteMessages'] = pydantic.Field(
        'types.UpdateDeleteMessages',
        alias='_'
    )

    messages: list[int]
    pts: int
    pts_count: int
