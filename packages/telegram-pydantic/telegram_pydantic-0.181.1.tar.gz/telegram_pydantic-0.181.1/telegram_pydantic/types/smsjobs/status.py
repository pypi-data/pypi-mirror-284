from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Status(BaseModel):
    """
    types.smsjobs.Status
    ID: 0x2aee9191
    Layer: 181
    """
    QUALNAME: typing.Literal['types.smsjobs.Status'] = pydantic.Field(
        'types.smsjobs.Status',
        alias='_'
    )

    recent_sent: int
    recent_since: int
    recent_remains: int
    total_sent: int
    total_since: int
    terms_url: str
    allow_international: typing.Optional[bool] = None
    last_gift_slug: typing.Optional[str] = None
