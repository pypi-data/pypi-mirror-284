from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetContactSignUpNotification(BaseModel):
    """
    functions.account.GetContactSignUpNotification
    ID: 0x9f07c728
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetContactSignUpNotification'] = pydantic.Field(
        'functions.account.GetContactSignUpNotification',
        alias='_'
    )

