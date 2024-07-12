from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageUploadRoundAction(BaseModel):
    """
    types.SendMessageUploadRoundAction
    ID: 0x243e1c66
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageUploadRoundAction'] = pydantic.Field(
        'types.SendMessageUploadRoundAction',
        alias='_'
    )

    progress: int
