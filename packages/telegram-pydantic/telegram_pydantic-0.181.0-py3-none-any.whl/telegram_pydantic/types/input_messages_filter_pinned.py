from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterPinned(BaseModel):
    """
    types.InputMessagesFilterPinned
    ID: 0x1bb00451
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterPinned'] = pydantic.Field(
        'types.InputMessagesFilterPinned',
        alias='_'
    )

