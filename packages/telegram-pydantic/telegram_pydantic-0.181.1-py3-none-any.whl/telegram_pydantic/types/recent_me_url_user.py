from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecentMeUrlUser(BaseModel):
    """
    types.RecentMeUrlUser
    ID: 0xb92c09e2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RecentMeUrlUser'] = pydantic.Field(
        'types.RecentMeUrlUser',
        alias='_'
    )

    url: str
    user_id: int
