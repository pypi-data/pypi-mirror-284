from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestPasswordRecovery(BaseModel):
    """
    functions.auth.RequestPasswordRecovery
    ID: 0xd897bc66
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.RequestPasswordRecovery'] = pydantic.Field(
        'functions.auth.RequestPasswordRecovery',
        alias='_'
    )

