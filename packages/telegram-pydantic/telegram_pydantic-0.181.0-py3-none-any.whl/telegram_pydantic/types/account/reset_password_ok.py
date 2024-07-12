from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetPasswordOk(BaseModel):
    """
    types.account.ResetPasswordOk
    ID: 0xe926d63e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.ResetPasswordOk'] = pydantic.Field(
        'types.account.ResetPasswordOk',
        alias='_'
    )

