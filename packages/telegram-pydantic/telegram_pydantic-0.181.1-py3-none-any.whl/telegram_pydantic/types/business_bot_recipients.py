from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessBotRecipients(BaseModel):
    """
    types.BusinessBotRecipients
    ID: 0xb88cf373
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessBotRecipients'] = pydantic.Field(
        'types.BusinessBotRecipients',
        alias='_'
    )

    existing_chats: typing.Optional[bool] = None
    new_chats: typing.Optional[bool] = None
    contacts: typing.Optional[bool] = None
    non_contacts: typing.Optional[bool] = None
    exclude_selected: typing.Optional[bool] = None
    users: typing.Optional[list[int]] = None
    exclude_users: typing.Optional[list[int]] = None
