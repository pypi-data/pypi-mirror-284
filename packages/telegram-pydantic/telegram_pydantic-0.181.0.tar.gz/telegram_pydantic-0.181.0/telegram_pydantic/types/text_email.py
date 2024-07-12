from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextEmail(BaseModel):
    """
    types.TextEmail
    ID: 0xde5a0dd6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextEmail'] = pydantic.Field(
        'types.TextEmail',
        alias='_'
    )

    text: "base.RichText"
    email: str
