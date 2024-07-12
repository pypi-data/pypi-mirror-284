from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPasswordSettings(BaseModel):
    """
    functions.account.GetPasswordSettings
    ID: 0x9cd4eaf9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetPasswordSettings'] = pydantic.Field(
        'functions.account.GetPasswordSettings',
        alias='_'
    )

    password: "base.InputCheckPasswordSRP"
