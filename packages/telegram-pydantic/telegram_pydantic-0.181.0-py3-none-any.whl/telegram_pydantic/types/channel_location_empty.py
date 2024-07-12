from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelLocationEmpty(BaseModel):
    """
    types.ChannelLocationEmpty
    ID: 0xbfb5ad8b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelLocationEmpty'] = pydantic.Field(
        'types.ChannelLocationEmpty',
        alias='_'
    )

