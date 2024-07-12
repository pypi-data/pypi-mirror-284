from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputClientProxy(BaseModel):
    """
    types.InputClientProxy
    ID: 0x75588b3f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputClientProxy'] = pydantic.Field(
        'types.InputClientProxy',
        alias='_'
    )

    address: str
    port: int
