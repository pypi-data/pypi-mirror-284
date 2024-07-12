from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuBot(BaseModel):
    """
    types.AttachMenuBot
    ID: 0xd90d8dfe
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuBot'] = pydantic.Field(
        'types.AttachMenuBot',
        alias='_'
    )

    bot_id: int
    short_name: str
    icons: list["base.AttachMenuBotIcon"]
    inactive: typing.Optional[bool] = None
    has_settings: typing.Optional[bool] = None
    request_write_access: typing.Optional[bool] = None
    show_in_attach_menu: typing.Optional[bool] = None
    show_in_side_menu: typing.Optional[bool] = None
    side_menu_disclaimer_needed: typing.Optional[bool] = None
    peer_types: typing.Optional[list["base.AttachMenuPeerType"]] = None
