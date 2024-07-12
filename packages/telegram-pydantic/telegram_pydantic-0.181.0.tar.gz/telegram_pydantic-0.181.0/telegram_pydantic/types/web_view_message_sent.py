from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebViewMessageSent(BaseModel):
    """
    types.WebViewMessageSent
    ID: 0xc94511c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebViewMessageSent'] = pydantic.Field(
        'types.WebViewMessageSent',
        alias='_'
    )

    msg_id: typing.Optional["base.InputBotInlineMessageID"] = None
