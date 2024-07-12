from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueDisallowContacts(BaseModel):
    """
    types.InputPrivacyValueDisallowContacts
    ID: 0xba52007
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueDisallowContacts'] = pydantic.Field(
        'types.InputPrivacyValueDisallowContacts',
        alias='_'
    )

