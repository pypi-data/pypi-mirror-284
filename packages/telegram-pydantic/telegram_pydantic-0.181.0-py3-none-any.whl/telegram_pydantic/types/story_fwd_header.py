from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryFwdHeader(BaseModel):
    """
    types.StoryFwdHeader
    ID: 0xb826e150
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryFwdHeader'] = pydantic.Field(
        'types.StoryFwdHeader',
        alias='_'
    )

    modified: typing.Optional[bool] = None
    from_peer: typing.Optional["base.Peer"] = pydantic.Field(None, alias='from')
    from_name: typing.Optional[str] = None
    story_id: typing.Optional[int] = None
