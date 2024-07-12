from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeletePhoneCallHistory(BaseModel):
    """
    functions.messages.DeletePhoneCallHistory
    ID: 0xf9cbe409
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeletePhoneCallHistory'] = pydantic.Field(
        'functions.messages.DeletePhoneCallHistory',
        alias='_'
    )

    revoke: typing.Optional[bool] = None
