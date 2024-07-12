from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetContentSettings(BaseModel):
    """
    functions.account.SetContentSettings
    ID: 0xb574b16b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SetContentSettings'] = pydantic.Field(
        'functions.account.SetContentSettings',
        alias='_'
    )

    sensitive_enabled: typing.Optional[bool] = None
