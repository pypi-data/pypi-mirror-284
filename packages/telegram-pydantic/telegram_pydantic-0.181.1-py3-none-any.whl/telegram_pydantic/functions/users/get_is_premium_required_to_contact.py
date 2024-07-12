from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetIsPremiumRequiredToContact(BaseModel):
    """
    functions.users.GetIsPremiumRequiredToContact
    ID: 0xa622aa10
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.users.GetIsPremiumRequiredToContact'] = pydantic.Field(
        'functions.users.GetIsPremiumRequiredToContact',
        alias='_'
    )

    id: list["base.InputUser"]
