from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessageID(BaseModel):
    """
    types.InputMessageID
    ID: 0xa676a322
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessageID'] = pydantic.Field(
        'types.InputMessageID',
        alias='_'
    )

    id: int
