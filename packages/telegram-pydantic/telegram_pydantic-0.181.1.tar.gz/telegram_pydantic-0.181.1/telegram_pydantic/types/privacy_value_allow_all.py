from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueAllowAll(BaseModel):
    """
    types.PrivacyValueAllowAll
    ID: 0x65427b82
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueAllowAll'] = pydantic.Field(
        'types.PrivacyValueAllowAll',
        alias='_'
    )

