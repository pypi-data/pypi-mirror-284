from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetTermsOfServiceUpdate(BaseModel):
    """
    functions.help.GetTermsOfServiceUpdate
    ID: 0x2ca51fd1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetTermsOfServiceUpdate'] = pydantic.Field(
        'functions.help.GetTermsOfServiceUpdate',
        alias='_'
    )

