from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeTitle(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeTitle
    ID: 0xe6dfb825
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeTitle'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeTitle',
        alias='_'
    )

    prev_value: str
    new_value: str
