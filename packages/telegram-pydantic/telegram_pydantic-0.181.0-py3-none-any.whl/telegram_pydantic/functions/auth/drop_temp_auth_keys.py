from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DropTempAuthKeys(BaseModel):
    """
    functions.auth.DropTempAuthKeys
    ID: 0x8e48a188
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.DropTempAuthKeys'] = pydantic.Field(
        'functions.auth.DropTempAuthKeys',
        alias='_'
    )

    except_auth_keys: list[int]
