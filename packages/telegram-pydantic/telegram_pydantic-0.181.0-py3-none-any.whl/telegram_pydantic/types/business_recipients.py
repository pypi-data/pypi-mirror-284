from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessRecipients(BaseModel):
    """
    types.BusinessRecipients
    ID: 0x21108ff7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessRecipients'] = pydantic.Field(
        'types.BusinessRecipients',
        alias='_'
    )

    existing_chats: typing.Optional[bool] = None
    new_chats: typing.Optional[bool] = None
    contacts: typing.Optional[bool] = None
    non_contacts: typing.Optional[bool] = None
    exclude_selected: typing.Optional[bool] = None
    users: typing.Optional[list[int]] = None
