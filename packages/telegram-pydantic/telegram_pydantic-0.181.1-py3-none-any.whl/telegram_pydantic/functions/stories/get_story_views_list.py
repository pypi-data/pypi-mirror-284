from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStoryViewsList(BaseModel):
    """
    functions.stories.GetStoryViewsList
    ID: 0x7ed23c57
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetStoryViewsList'] = pydantic.Field(
        'functions.stories.GetStoryViewsList',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
    offset: str
    limit: int
    just_contacts: typing.Optional[bool] = None
    reactions_first: typing.Optional[bool] = None
    forwards_first: typing.Optional[bool] = None
    q: typing.Optional[str] = None
