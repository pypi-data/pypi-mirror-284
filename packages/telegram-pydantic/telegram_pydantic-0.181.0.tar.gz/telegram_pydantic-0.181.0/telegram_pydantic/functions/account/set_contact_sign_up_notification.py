from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetContactSignUpNotification(BaseModel):
    """
    functions.account.SetContactSignUpNotification
    ID: 0xcff43f61
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SetContactSignUpNotification'] = pydantic.Field(
        'functions.account.SetContactSignUpNotification',
        alias='_'
    )

    silent: bool
