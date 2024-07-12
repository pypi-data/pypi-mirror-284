from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAllStories(BaseModel):
    """
    functions.stories.GetAllStories
    ID: 0xeeb0d625
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetAllStories'] = pydantic.Field(
        'functions.stories.GetAllStories',
        alias='_'
    )

    next: typing.Optional[bool] = None
    hidden: typing.Optional[bool] = None
    state: typing.Optional[str] = None
