from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAllReadPeerStories(BaseModel):
    """
    functions.stories.GetAllReadPeerStories
    ID: 0x9b5ae7f9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetAllReadPeerStories'] = pydantic.Field(
        'functions.stories.GetAllReadPeerStories',
        alias='_'
    )

