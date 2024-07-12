from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# KeyboardButton - Layer 181
KeyboardButton = typing.Annotated[
    typing.Union[
        types.InputKeyboardButtonRequestPeer,
        types.InputKeyboardButtonUrlAuth,
        types.InputKeyboardButtonUserProfile,
        types.KeyboardButton,
        types.KeyboardButtonBuy,
        types.KeyboardButtonCallback,
        types.KeyboardButtonGame,
        types.KeyboardButtonRequestGeoLocation,
        types.KeyboardButtonRequestPeer,
        types.KeyboardButtonRequestPhone,
        types.KeyboardButtonRequestPoll,
        types.KeyboardButtonSimpleWebView,
        types.KeyboardButtonSwitchInline,
        types.KeyboardButtonUrl,
        types.KeyboardButtonUrlAuth,
        types.KeyboardButtonUserProfile,
        types.KeyboardButtonWebView
    ],
    pydantic.Field(discriminator='QUALNAME')
]
