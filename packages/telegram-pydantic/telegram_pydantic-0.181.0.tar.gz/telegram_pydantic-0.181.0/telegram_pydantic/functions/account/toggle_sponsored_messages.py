from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleSponsoredMessages(BaseModel):
    """
    functions.account.ToggleSponsoredMessages
    ID: 0xb9d9a38d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ToggleSponsoredMessages'] = pydantic.Field(
        'functions.account.ToggleSponsoredMessages',
        alias='_'
    )

    enabled: bool
