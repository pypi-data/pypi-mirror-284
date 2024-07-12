from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Username(BaseModel):
    """
    types.Username
    ID: 0xb4073647
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Username'] = pydantic.Field(
        'types.Username',
        alias='_'
    )

    username: str
    editable: typing.Optional[bool] = None
    active: typing.Optional[bool] = None
