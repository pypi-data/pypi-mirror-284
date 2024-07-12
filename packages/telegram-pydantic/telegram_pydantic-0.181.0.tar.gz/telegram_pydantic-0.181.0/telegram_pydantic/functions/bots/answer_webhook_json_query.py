from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AnswerWebhookJSONQuery(BaseModel):
    """
    functions.bots.AnswerWebhookJSONQuery
    ID: 0xe6213f4d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.AnswerWebhookJSONQuery'] = pydantic.Field(
        'functions.bots.AnswerWebhookJSONQuery',
        alias='_'
    )

    query_id: int
    data: "base.DataJSON"
