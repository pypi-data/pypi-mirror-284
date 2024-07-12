from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallEmpty(BaseModel):
    """
    types.PhoneCallEmpty
    ID: 0x5366c915
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallEmpty'] = pydantic.Field(
        'types.PhoneCallEmpty',
        alias='_'
    )

    id: int
