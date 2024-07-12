from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetPasswordRequestedWait(BaseModel):
    """
    types.account.ResetPasswordRequestedWait
    ID: 0xe9effc7d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.ResetPasswordRequestedWait'] = pydantic.Field(
        'types.account.ResetPasswordRequestedWait',
        alias='_'
    )

    until_date: int
