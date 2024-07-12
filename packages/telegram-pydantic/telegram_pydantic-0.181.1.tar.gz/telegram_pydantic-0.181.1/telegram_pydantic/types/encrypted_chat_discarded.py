from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedChatDiscarded(BaseModel):
    """
    types.EncryptedChatDiscarded
    ID: 0x1e1c7c45
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedChatDiscarded'] = pydantic.Field(
        'types.EncryptedChatDiscarded',
        alias='_'
    )

    id: int
    history_deleted: typing.Optional[bool] = None
