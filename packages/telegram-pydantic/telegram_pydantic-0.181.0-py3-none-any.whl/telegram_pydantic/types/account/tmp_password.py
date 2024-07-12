from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TmpPassword(BaseModel):
    """
    types.account.TmpPassword
    ID: 0xdb64fd34
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.TmpPassword'] = pydantic.Field(
        'types.account.TmpPassword',
        alias='_'
    )

    tmp_password: bytes
    valid_until: int
