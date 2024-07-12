from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionContactSignUp(BaseModel):
    """
    types.MessageActionContactSignUp
    ID: 0xf3f25f76
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionContactSignUp'] = pydantic.Field(
        'types.MessageActionContactSignUp',
        alias='_'
    )

