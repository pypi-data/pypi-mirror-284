from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterMyMentions(BaseModel):
    """
    types.InputMessagesFilterMyMentions
    ID: 0xc1f8e69a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterMyMentions'] = pydantic.Field(
        'types.InputMessagesFilterMyMentions',
        alias='_'
    )

