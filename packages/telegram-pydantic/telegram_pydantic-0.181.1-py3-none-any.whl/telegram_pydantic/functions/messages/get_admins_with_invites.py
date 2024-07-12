from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAdminsWithInvites(BaseModel):
    """
    functions.messages.GetAdminsWithInvites
    ID: 0x3920e6ef
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetAdminsWithInvites'] = pydantic.Field(
        'functions.messages.GetAdminsWithInvites',
        alias='_'
    )

    peer: "base.InputPeer"
