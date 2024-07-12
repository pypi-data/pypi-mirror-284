from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InlineQueryPeerTypeSameBotPM(BaseModel):
    """
    types.InlineQueryPeerTypeSameBotPM
    ID: 0x3081ed9d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InlineQueryPeerTypeSameBotPM'] = pydantic.Field(
        'types.InlineQueryPeerTypeSameBotPM',
        alias='_'
    )

