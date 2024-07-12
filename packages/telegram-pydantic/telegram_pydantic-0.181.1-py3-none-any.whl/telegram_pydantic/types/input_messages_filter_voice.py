from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterVoice(BaseModel):
    """
    types.InputMessagesFilterVoice
    ID: 0x50f5c392
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterVoice'] = pydantic.Field(
        'types.InputMessagesFilterVoice',
        alias='_'
    )

