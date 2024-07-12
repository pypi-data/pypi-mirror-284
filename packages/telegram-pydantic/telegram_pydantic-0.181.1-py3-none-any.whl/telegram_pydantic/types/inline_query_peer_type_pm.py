from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InlineQueryPeerTypePM(BaseModel):
    """
    types.InlineQueryPeerTypePM
    ID: 0x833c0fac
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InlineQueryPeerTypePM'] = pydantic.Field(
        'types.InlineQueryPeerTypePM',
        alias='_'
    )

