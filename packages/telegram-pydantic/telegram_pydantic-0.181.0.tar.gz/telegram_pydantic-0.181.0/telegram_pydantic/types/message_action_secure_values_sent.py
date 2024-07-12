from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionSecureValuesSent(BaseModel):
    """
    types.MessageActionSecureValuesSent
    ID: 0xd95c6154
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionSecureValuesSent'] = pydantic.Field(
        'types.MessageActionSecureValuesSent',
        alias='_'
    )

    types: list["base.SecureValueType"]
