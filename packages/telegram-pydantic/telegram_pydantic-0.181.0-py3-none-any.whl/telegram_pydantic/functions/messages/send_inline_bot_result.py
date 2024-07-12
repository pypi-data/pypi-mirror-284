from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendInlineBotResult(BaseModel):
    """
    functions.messages.SendInlineBotResult
    ID: 0x3ebee86a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendInlineBotResult'] = pydantic.Field(
        'functions.messages.SendInlineBotResult',
        alias='_'
    )

    peer: "base.InputPeer"
    random_id: int
    query_id: int
    id: str
    silent: typing.Optional[bool] = None
    background: typing.Optional[bool] = None
    clear_draft: typing.Optional[bool] = None
    hide_via: typing.Optional[bool] = None
    reply_to: typing.Optional["base.InputReplyTo"] = None
    schedule_date: typing.Optional[int] = None
    send_as: typing.Optional["base.InputPeer"] = None
    quick_reply_shortcut: typing.Optional["base.InputQuickReplyShortcut"] = None
