from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetPasswordFailedWait(BaseModel):
    """
    types.account.ResetPasswordFailedWait
    ID: 0xe3779861
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.ResetPasswordFailedWait'] = pydantic.Field(
        'types.account.ResetPasswordFailedWait',
        alias='_'
    )

    retry_date: int
