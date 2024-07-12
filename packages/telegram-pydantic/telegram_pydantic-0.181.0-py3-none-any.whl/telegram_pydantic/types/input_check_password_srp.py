from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputCheckPasswordSRP(BaseModel):
    """
    types.InputCheckPasswordSRP
    ID: 0xd27ff082
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputCheckPasswordSRP'] = pydantic.Field(
        'types.InputCheckPasswordSRP',
        alias='_'
    )

    srp_id: int
    A: bytes
    M1: bytes
