from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyAbout(BaseModel):
    """
    types.PrivacyKeyAbout
    ID: 0xa486b761
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyAbout'] = pydantic.Field(
        'types.PrivacyKeyAbout',
        alias='_'
    )

