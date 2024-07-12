from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateMessageID(BaseModel):
    """
    types.UpdateMessageID
    ID: 0x4e90bfd6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateMessageID'] = pydantic.Field(
        'types.UpdateMessageID',
        alias='_'
    )

    id: int
    random_id: int
