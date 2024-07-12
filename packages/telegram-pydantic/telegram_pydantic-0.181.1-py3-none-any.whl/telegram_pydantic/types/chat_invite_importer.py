from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatInviteImporter(BaseModel):
    """
    types.ChatInviteImporter
    ID: 0x8c5adfd9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatInviteImporter'] = pydantic.Field(
        'types.ChatInviteImporter',
        alias='_'
    )

    user_id: int
    date: int
    requested: typing.Optional[bool] = None
    via_chatlist: typing.Optional[bool] = None
    about: typing.Optional[str] = None
    approved_by: typing.Optional[int] = None
