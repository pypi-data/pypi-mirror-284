from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionUpdatePinned(BaseModel):
    """
    types.ChannelAdminLogEventActionUpdatePinned
    ID: 0xe9e82c18
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionUpdatePinned'] = pydantic.Field(
        'types.ChannelAdminLogEventActionUpdatePinned',
        alias='_'
    )

    message: "base.Message"
