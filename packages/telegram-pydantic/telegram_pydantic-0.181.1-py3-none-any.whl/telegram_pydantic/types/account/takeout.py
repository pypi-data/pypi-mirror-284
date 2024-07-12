from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Takeout(BaseModel):
    """
    types.account.Takeout
    ID: 0x4dba4501
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.Takeout'] = pydantic.Field(
        'types.account.Takeout',
        alias='_'
    )

    id: int
