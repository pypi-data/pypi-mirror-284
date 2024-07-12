from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeSetUpEmailRequired(BaseModel):
    """
    types.auth.SentCodeTypeSetUpEmailRequired
    ID: 0xa5491dea
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeSetUpEmailRequired'] = pydantic.Field(
        'types.auth.SentCodeTypeSetUpEmailRequired',
        alias='_'
    )

    apple_signin_allowed: typing.Optional[bool] = None
    google_signin_allowed: typing.Optional[bool] = None
