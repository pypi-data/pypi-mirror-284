from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebAuthorization(BaseModel):
    """
    types.WebAuthorization
    ID: 0xa6f8f452
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebAuthorization'] = pydantic.Field(
        'types.WebAuthorization',
        alias='_'
    )

    hash: int
    bot_id: int
    domain: str
    browser: str
    platform: str
    date_created: int
    date_active: int
    ip: str
    region: str
