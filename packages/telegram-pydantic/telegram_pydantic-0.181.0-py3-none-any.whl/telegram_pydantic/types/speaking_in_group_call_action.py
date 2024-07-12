from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SpeakingInGroupCallAction(BaseModel):
    """
    types.SpeakingInGroupCallAction
    ID: 0xd92c2285
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SpeakingInGroupCallAction'] = pydantic.Field(
        'types.SpeakingInGroupCallAction',
        alias='_'
    )

