from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EligibleToJoin(BaseModel):
    """
    types.smsjobs.EligibleToJoin
    ID: 0xdc8b44cf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.smsjobs.EligibleToJoin'] = pydantic.Field(
        'types.smsjobs.EligibleToJoin',
        alias='_'
    )

    terms_url: str
    monthly_sent_sms: int
