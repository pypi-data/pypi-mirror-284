from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateEditMessage(BaseModel):
    """
    types.UpdateEditMessage
    ID: 0xe40370a3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateEditMessage'] = pydantic.Field(
        'types.UpdateEditMessage',
        alias='_'
    )

    message: "base.Message"
    pts: int
    pts_count: int
