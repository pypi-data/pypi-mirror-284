from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyAbout(BaseModel):
    """
    types.InputPrivacyKeyAbout
    ID: 0x3823cc40
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyAbout'] = pydantic.Field(
        'types.InputPrivacyKeyAbout',
        alias='_'
    )

