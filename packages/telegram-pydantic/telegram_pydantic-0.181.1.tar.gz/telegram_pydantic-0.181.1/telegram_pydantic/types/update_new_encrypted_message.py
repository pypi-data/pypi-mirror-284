from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNewEncryptedMessage(BaseModel):
    """
    types.UpdateNewEncryptedMessage
    ID: 0x12bcbd9a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateNewEncryptedMessage'] = pydantic.Field(
        'types.UpdateNewEncryptedMessage',
        alias='_'
    )

    message: "base.EncryptedMessage"
    qts: int
