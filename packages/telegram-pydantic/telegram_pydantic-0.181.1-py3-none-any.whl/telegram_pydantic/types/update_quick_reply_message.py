from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateQuickReplyMessage(BaseModel):
    """
    types.UpdateQuickReplyMessage
    ID: 0x3e050d0f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateQuickReplyMessage'] = pydantic.Field(
        'types.UpdateQuickReplyMessage',
        alias='_'
    )

    message: "base.Message"
