from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetInviteText(BaseModel):
    """
    functions.help.GetInviteText
    ID: 0x4d392343
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetInviteText'] = pydantic.Field(
        'functions.help.GetInviteText',
        alias='_'
    )

