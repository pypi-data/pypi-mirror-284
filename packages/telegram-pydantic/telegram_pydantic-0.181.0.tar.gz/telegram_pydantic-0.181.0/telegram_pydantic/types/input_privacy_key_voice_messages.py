from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyVoiceMessages(BaseModel):
    """
    types.InputPrivacyKeyVoiceMessages
    ID: 0xaee69d68
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyVoiceMessages'] = pydantic.Field(
        'types.InputPrivacyKeyVoiceMessages',
        alias='_'
    )

