from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGroupsForDiscussion(BaseModel):
    """
    functions.channels.GetGroupsForDiscussion
    ID: 0xf5dad378
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetGroupsForDiscussion'] = pydantic.Field(
        'functions.channels.GetGroupsForDiscussion',
        alias='_'
    )

