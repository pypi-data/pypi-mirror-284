from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueDisallowUsers(BaseModel):
    """
    types.InputPrivacyValueDisallowUsers
    ID: 0x90110467
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueDisallowUsers'] = pydantic.Field(
        'types.InputPrivacyValueDisallowUsers',
        alias='_'
    )

    users: list["base.InputUser"]
