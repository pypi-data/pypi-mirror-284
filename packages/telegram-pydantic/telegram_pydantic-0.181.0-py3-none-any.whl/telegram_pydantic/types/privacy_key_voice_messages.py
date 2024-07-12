from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyVoiceMessages(BaseModel):
    """
    types.PrivacyKeyVoiceMessages
    ID: 0x697f414
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyVoiceMessages'] = pydantic.Field(
        'types.PrivacyKeyVoiceMessages',
        alias='_'
    )

