from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueAllowContacts(BaseModel):
    """
    types.PrivacyValueAllowContacts
    ID: 0xfffe1bac
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueAllowContacts'] = pydantic.Field(
        'types.PrivacyValueAllowContacts',
        alias='_'
    )

