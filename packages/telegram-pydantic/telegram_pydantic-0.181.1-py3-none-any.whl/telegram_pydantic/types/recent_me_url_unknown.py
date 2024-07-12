from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecentMeUrlUnknown(BaseModel):
    """
    types.RecentMeUrlUnknown
    ID: 0x46e1d13d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RecentMeUrlUnknown'] = pydantic.Field(
        'types.RecentMeUrlUnknown',
        alias='_'
    )

    url: str
