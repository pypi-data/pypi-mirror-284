from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputGroupCall(BaseModel):
    """
    types.InputGroupCall
    ID: 0xd8aa840f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputGroupCall'] = pydantic.Field(
        'types.InputGroupCall',
        alias='_'
    )

    id: int
    access_hash: int
