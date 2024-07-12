from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UrlAuthResultRequest(BaseModel):
    """
    types.UrlAuthResultRequest
    ID: 0x92d33a0e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UrlAuthResultRequest'] = pydantic.Field(
        'types.UrlAuthResultRequest',
        alias='_'
    )

    bot: "base.User"
    domain: str
    request_write_access: typing.Optional[bool] = None
