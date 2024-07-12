from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueDisallowAll(BaseModel):
    """
    types.InputPrivacyValueDisallowAll
    ID: 0xd66b66c9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueDisallowAll'] = pydantic.Field(
        'types.InputPrivacyValueDisallowAll',
        alias='_'
    )

