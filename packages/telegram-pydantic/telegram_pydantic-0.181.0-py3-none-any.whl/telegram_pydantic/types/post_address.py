from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PostAddress(BaseModel):
    """
    types.PostAddress
    ID: 0x1e8caaeb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PostAddress'] = pydantic.Field(
        'types.PostAddress',
        alias='_'
    )

    street_line1: str
    street_line2: str
    city: str
    state: str
    country_iso2: str
    post_code: str
