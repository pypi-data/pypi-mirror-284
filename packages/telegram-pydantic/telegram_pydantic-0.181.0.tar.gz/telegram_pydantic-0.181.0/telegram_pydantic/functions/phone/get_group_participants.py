from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGroupParticipants(BaseModel):
    """
    functions.phone.GetGroupParticipants
    ID: 0xc558d8ab
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.GetGroupParticipants'] = pydantic.Field(
        'functions.phone.GetGroupParticipants',
        alias='_'
    )

    call: "base.InputGroupCall"
    ids: list["base.InputPeer"]
    sources: list[int]
    offset: str
    limit: int
