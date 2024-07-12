from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMessageReactionsList(BaseModel):
    """
    functions.messages.GetMessageReactionsList
    ID: 0x461b3f48
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetMessageReactionsList'] = pydantic.Field(
        'functions.messages.GetMessageReactionsList',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
    limit: int
    reaction: typing.Optional["base.Reaction"] = None
    offset: typing.Optional[str] = None
