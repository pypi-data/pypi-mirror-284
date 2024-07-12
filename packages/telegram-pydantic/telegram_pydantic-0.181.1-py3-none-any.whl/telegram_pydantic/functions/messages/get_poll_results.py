from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPollResults(BaseModel):
    """
    functions.messages.GetPollResults
    ID: 0x73bb643b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetPollResults'] = pydantic.Field(
        'functions.messages.GetPollResults',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
