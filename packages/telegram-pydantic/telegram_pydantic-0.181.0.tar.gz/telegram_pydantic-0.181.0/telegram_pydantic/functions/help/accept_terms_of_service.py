from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AcceptTermsOfService(BaseModel):
    """
    functions.help.AcceptTermsOfService
    ID: 0xee72f79a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.AcceptTermsOfService'] = pydantic.Field(
        'functions.help.AcceptTermsOfService',
        alias='_'
    )

    id: "base.DataJSON"
