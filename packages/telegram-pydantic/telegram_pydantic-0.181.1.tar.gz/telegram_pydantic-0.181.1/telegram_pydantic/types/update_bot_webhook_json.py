from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotWebhookJSON(BaseModel):
    """
    types.UpdateBotWebhookJSON
    ID: 0x8317c0c3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotWebhookJSON'] = pydantic.Field(
        'types.UpdateBotWebhookJSON',
        alias='_'
    )

    data: "base.DataJSON"
