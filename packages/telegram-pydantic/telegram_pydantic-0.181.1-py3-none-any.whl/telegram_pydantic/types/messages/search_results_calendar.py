from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchResultsCalendar(BaseModel):
    """
    types.messages.SearchResultsCalendar
    ID: 0x147ee23c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SearchResultsCalendar'] = pydantic.Field(
        'types.messages.SearchResultsCalendar',
        alias='_'
    )

    count: int
    min_date: int
    min_msg_id: int
    periods: list["base.SearchResultsCalendarPeriod"]
    messages: list["base.Message"]
    chats: list["base.Chat"]
    users: list["base.User"]
    inexact: typing.Optional[bool] = None
    offset_id_offset: typing.Optional[int] = None
