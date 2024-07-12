from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedGroupCallInvite(BaseModel):
    """
    types.phone.ExportedGroupCallInvite
    ID: 0x204bd158
    Layer: 181
    """
    QUALNAME: typing.Literal['types.phone.ExportedGroupCallInvite'] = pydantic.Field(
        'types.phone.ExportedGroupCallInvite',
        alias='_'
    )

    link: str
