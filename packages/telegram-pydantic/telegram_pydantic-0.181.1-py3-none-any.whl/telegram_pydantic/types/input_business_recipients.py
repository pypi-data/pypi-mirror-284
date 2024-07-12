from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBusinessRecipients(BaseModel):
    """
    types.InputBusinessRecipients
    ID: 0x6f8b32aa
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBusinessRecipients'] = pydantic.Field(
        'types.InputBusinessRecipients',
        alias='_'
    )

    existing_chats: typing.Optional[bool] = None
    new_chats: typing.Optional[bool] = None
    contacts: typing.Optional[bool] = None
    non_contacts: typing.Optional[bool] = None
    exclude_selected: typing.Optional[bool] = None
    users: typing.Optional[list["base.InputUser"]] = None
