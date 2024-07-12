from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterRoundVoice(BaseModel):
    """
    types.InputMessagesFilterRoundVoice
    ID: 0x7a7c17a4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterRoundVoice'] = pydantic.Field(
        'types.InputMessagesFilterRoundVoice',
        alias='_'
    )

