from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GroupCallParticipantVideoSourceGroup(BaseModel):
    """
    types.GroupCallParticipantVideoSourceGroup
    ID: 0xdcb118b7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.GroupCallParticipantVideoSourceGroup'] = pydantic.Field(
        'types.GroupCallParticipantVideoSourceGroup',
        alias='_'
    )

    semantics: str
    sources: list[int]
