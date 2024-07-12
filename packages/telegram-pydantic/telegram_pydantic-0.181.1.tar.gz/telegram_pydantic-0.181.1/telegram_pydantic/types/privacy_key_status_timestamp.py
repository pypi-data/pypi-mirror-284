from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyStatusTimestamp(BaseModel):
    """
    types.PrivacyKeyStatusTimestamp
    ID: 0xbc2eab30
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyStatusTimestamp'] = pydantic.Field(
        'types.PrivacyKeyStatusTimestamp',
        alias='_'
    )

