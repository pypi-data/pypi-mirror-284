from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelMessagesFilter(BaseModel):
    """
    types.ChannelMessagesFilter
    ID: 0xcd77d957
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelMessagesFilter'] = pydantic.Field(
        'types.ChannelMessagesFilter',
        alias='_'
    )

    ranges: list["base.MessageRange"]
    exclude_new_messages: typing.Optional[bool] = None
