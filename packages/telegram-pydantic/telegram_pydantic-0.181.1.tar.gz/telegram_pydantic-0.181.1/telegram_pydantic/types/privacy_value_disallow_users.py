from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueDisallowUsers(BaseModel):
    """
    types.PrivacyValueDisallowUsers
    ID: 0xe4621141
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueDisallowUsers'] = pydantic.Field(
        'types.PrivacyValueDisallowUsers',
        alias='_'
    )

    users: list[int]
