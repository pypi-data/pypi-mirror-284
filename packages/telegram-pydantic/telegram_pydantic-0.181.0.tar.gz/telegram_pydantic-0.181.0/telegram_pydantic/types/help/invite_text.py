from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InviteText(BaseModel):
    """
    types.help.InviteText
    ID: 0x18cb9f78
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.InviteText'] = pydantic.Field(
        'types.help.InviteText',
        alias='_'
    )

    message: str
