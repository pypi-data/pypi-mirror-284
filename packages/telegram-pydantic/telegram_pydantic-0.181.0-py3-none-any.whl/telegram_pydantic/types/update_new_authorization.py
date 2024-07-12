from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNewAuthorization(BaseModel):
    """
    types.UpdateNewAuthorization
    ID: 0x8951abef
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateNewAuthorization'] = pydantic.Field(
        'types.UpdateNewAuthorization',
        alias='_'
    )

    hash: int
    unconfirmed: typing.Optional[bool] = None
    date: typing.Optional[int] = None
    device: typing.Optional[str] = None
    location: typing.Optional[str] = None
