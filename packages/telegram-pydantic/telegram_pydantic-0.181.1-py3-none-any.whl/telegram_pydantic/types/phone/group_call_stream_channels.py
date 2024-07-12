from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GroupCallStreamChannels(BaseModel):
    """
    types.phone.GroupCallStreamChannels
    ID: 0xd0e482b2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.phone.GroupCallStreamChannels'] = pydantic.Field(
        'types.phone.GroupCallStreamChannels',
        alias='_'
    )

    channels: list["base.GroupCallStreamChannel"]
