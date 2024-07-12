from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotCommandScopeChatAdmins(BaseModel):
    """
    types.BotCommandScopeChatAdmins
    ID: 0xb9aa606a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotCommandScopeChatAdmins'] = pydantic.Field(
        'types.BotCommandScopeChatAdmins',
        alias='_'
    )

