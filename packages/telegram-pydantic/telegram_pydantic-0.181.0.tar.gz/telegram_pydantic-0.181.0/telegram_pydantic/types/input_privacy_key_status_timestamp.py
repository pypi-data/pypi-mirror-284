from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyStatusTimestamp(BaseModel):
    """
    types.InputPrivacyKeyStatusTimestamp
    ID: 0x4f96cb18
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyStatusTimestamp'] = pydantic.Field(
        'types.InputPrivacyKeyStatusTimestamp',
        alias='_'
    )

