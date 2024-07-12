from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonCallback(BaseModel):
    """
    types.KeyboardButtonCallback
    ID: 0x35bbdb6b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonCallback'] = pydantic.Field(
        'types.KeyboardButtonCallback',
        alias='_'
    )

    text: str
    data: bytes
    requires_password: typing.Optional[bool] = None
