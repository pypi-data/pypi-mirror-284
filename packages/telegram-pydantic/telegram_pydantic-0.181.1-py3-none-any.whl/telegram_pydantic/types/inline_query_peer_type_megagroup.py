from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InlineQueryPeerTypeMegagroup(BaseModel):
    """
    types.InlineQueryPeerTypeMegagroup
    ID: 0x5ec4be43
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InlineQueryPeerTypeMegagroup'] = pydantic.Field(
        'types.InlineQueryPeerTypeMegagroup',
        alias='_'
    )

