from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterContacts(BaseModel):
    """
    types.InputMessagesFilterContacts
    ID: 0xe062db83
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterContacts'] = pydantic.Field(
        'types.InputMessagesFilterContacts',
        alias='_'
    )

