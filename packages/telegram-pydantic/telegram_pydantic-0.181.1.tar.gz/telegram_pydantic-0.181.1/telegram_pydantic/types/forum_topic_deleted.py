from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ForumTopicDeleted(BaseModel):
    """
    types.ForumTopicDeleted
    ID: 0x23f109b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ForumTopicDeleted'] = pydantic.Field(
        'types.ForumTopicDeleted',
        alias='_'
    )

    id: int
