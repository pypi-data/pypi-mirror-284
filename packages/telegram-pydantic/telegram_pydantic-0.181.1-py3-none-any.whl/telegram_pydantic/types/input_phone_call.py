from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPhoneCall(BaseModel):
    """
    types.InputPhoneCall
    ID: 0x1e36fded
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPhoneCall'] = pydantic.Field(
        'types.InputPhoneCall',
        alias='_'
    )

    id: int
    access_hash: int
