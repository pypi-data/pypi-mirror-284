from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueDisallowContacts(BaseModel):
    """
    types.PrivacyValueDisallowContacts
    ID: 0xf888fa1a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueDisallowContacts'] = pydantic.Field(
        'types.PrivacyValueDisallowContacts',
        alias='_'
    )

