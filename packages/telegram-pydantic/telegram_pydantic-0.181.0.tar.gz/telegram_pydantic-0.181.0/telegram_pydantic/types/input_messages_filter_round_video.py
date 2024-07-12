from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterRoundVideo(BaseModel):
    """
    types.InputMessagesFilterRoundVideo
    ID: 0xb549da53
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterRoundVideo'] = pydantic.Field(
        'types.InputMessagesFilterRoundVideo',
        alias='_'
    )

