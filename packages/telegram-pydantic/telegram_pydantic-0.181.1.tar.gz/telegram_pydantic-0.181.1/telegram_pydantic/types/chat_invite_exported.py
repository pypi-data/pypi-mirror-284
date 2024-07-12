from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatInviteExported(BaseModel):
    """
    types.ChatInviteExported
    ID: 0xab4a819
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatInviteExported'] = pydantic.Field(
        'types.ChatInviteExported',
        alias='_'
    )

    link: str
    admin_id: int
    date: int
    revoked: typing.Optional[bool] = None
    permanent: typing.Optional[bool] = None
    request_needed: typing.Optional[bool] = None
    start_date: typing.Optional[int] = None
    expire_date: typing.Optional[int] = None
    usage_limit: typing.Optional[int] = None
    usage: typing.Optional[int] = None
    requested: typing.Optional[int] = None
    title: typing.Optional[str] = None
