from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetDiscussionGroup(BaseModel):
    """
    functions.channels.SetDiscussionGroup
    ID: 0x40582bb2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.SetDiscussionGroup'] = pydantic.Field(
        'functions.channels.SetDiscussionGroup',
        alias='_'
    )

    broadcast: "base.InputChannel"
    group: "base.InputChannel"
