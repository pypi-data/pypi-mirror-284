from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeSuccess(BaseModel):
    """
    types.auth.SentCodeSuccess
    ID: 0x2390fe44
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeSuccess'] = pydantic.Field(
        'types.auth.SentCodeSuccess',
        alias='_'
    )

    authorization: "base.auth.Authorization"
