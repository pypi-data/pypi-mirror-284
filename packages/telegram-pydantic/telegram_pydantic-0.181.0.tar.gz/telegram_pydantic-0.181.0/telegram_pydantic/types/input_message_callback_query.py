from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessageCallbackQuery(BaseModel):
    """
    types.InputMessageCallbackQuery
    ID: 0xacfa1a7e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessageCallbackQuery'] = pydantic.Field(
        'types.InputMessageCallbackQuery',
        alias='_'
    )

    id: int
    query_id: int
