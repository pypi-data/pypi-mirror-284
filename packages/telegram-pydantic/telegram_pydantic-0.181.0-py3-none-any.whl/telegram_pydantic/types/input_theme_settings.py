from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputThemeSettings(BaseModel):
    """
    types.InputThemeSettings
    ID: 0x8fde504f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputThemeSettings'] = pydantic.Field(
        'types.InputThemeSettings',
        alias='_'
    )

    base_theme: "base.BaseTheme"
    accent_color: int
    message_colors_animated: typing.Optional[bool] = None
    outbox_accent_color: typing.Optional[int] = None
    message_colors: typing.Optional[list[int]] = None
    wallpaper: typing.Optional["base.InputWallPaper"] = None
    wallpaper_settings: typing.Optional["base.WallPaperSettings"] = None
