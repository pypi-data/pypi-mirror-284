from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeSmsPhrase(BaseModel):
    """
    types.auth.SentCodeTypeSmsPhrase
    ID: 0xb37794af
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeSmsPhrase'] = pydantic.Field(
        'types.auth.SentCodeTypeSmsPhrase',
        alias='_'
    )

    beginning: typing.Optional[str] = None
