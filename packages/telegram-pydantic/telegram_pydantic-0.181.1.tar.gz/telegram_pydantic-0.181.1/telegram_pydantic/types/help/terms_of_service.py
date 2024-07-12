from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TermsOfService(BaseModel):
    """
    types.help.TermsOfService
    ID: 0x780a0310
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.TermsOfService'] = pydantic.Field(
        'types.help.TermsOfService',
        alias='_'
    )

    id: "base.DataJSON"
    text: str
    entities: list["base.MessageEntity"]
    popup: typing.Optional[bool] = None
    min_age_confirm: typing.Optional[int] = None
