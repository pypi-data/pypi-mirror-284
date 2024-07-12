from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNewMessage(BaseModel):
    """
    types.UpdateNewMessage
    ID: 0x1f2b0afd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateNewMessage'] = pydantic.Field(
        'types.UpdateNewMessage',
        alias='_'
    )

    message: "base.Message"
    pts: int
    pts_count: int
