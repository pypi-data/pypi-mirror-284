from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionGroupCall(BaseModel):
    """
    types.MessageActionGroupCall
    ID: 0x7a0d7f42
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionGroupCall'] = pydantic.Field(
        'types.MessageActionGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
    duration: typing.Optional[int] = None
