from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TermsOfServiceUpdate(BaseModel):
    """
    types.help.TermsOfServiceUpdate
    ID: 0x28ecf961
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.TermsOfServiceUpdate'] = pydantic.Field(
        'types.help.TermsOfServiceUpdate',
        alias='_'
    )

    expires: int
    terms_of_service: "base.help.TermsOfService"
