from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CodeTypeFragmentSms(BaseModel):
    """
    types.auth.CodeTypeFragmentSms
    ID: 0x6ed998c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.CodeTypeFragmentSms'] = pydantic.Field(
        'types.auth.CodeTypeFragmentSms',
        alias='_'
    )

