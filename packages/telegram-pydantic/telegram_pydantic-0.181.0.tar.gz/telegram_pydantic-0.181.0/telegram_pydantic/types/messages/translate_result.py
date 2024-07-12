from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TranslateResult(BaseModel):
    """
    types.messages.TranslateResult
    ID: 0x33db32f8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.TranslateResult'] = pydantic.Field(
        'types.messages.TranslateResult',
        alias='_'
    )

    result: list["base.TextWithEntities"]
