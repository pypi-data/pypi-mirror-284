from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotAppNotModified(BaseModel):
    """
    types.BotAppNotModified
    ID: 0x5da674b7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotAppNotModified'] = pydantic.Field(
        'types.BotAppNotModified',
        alias='_'
    )

