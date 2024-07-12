from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateProfile(BaseModel):
    """
    functions.account.UpdateProfile
    ID: 0x78515775
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateProfile'] = pydantic.Field(
        'functions.account.UpdateProfile',
        alias='_'
    )

    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    about: typing.Optional[str] = None
