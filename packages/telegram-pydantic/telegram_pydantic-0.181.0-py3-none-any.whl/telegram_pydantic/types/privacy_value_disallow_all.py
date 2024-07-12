from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueDisallowAll(BaseModel):
    """
    types.PrivacyValueDisallowAll
    ID: 0x8b73e763
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueDisallowAll'] = pydantic.Field(
        'types.PrivacyValueDisallowAll',
        alias='_'
    )

