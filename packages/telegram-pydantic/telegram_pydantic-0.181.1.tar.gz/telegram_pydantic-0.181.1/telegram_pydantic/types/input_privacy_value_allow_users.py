from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueAllowUsers(BaseModel):
    """
    types.InputPrivacyValueAllowUsers
    ID: 0x131cc67f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueAllowUsers'] = pydantic.Field(
        'types.InputPrivacyValueAllowUsers',
        alias='_'
    )

    users: list["base.InputUser"]
