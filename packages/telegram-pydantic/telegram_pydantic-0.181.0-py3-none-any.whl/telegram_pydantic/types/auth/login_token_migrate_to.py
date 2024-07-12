from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LoginTokenMigrateTo(BaseModel):
    """
    types.auth.LoginTokenMigrateTo
    ID: 0x68e9916
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.LoginTokenMigrateTo'] = pydantic.Field(
        'types.auth.LoginTokenMigrateTo',
        alias='_'
    )

    dc_id: int
    token: bytes
