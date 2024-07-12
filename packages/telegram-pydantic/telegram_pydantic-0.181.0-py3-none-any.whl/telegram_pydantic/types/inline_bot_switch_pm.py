from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InlineBotSwitchPM(BaseModel):
    """
    types.InlineBotSwitchPM
    ID: 0x3c20629f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InlineBotSwitchPM'] = pydantic.Field(
        'types.InlineBotSwitchPM',
        alias='_'
    )

    text: str
    start_param: str
