from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputStickerSet - Layer 181
InputStickerSet = typing.Annotated[
    typing.Union[
        types.InputStickerSetAnimatedEmoji,
        types.InputStickerSetAnimatedEmojiAnimations,
        types.InputStickerSetDice,
        types.InputStickerSetEmojiChannelDefaultStatuses,
        types.InputStickerSetEmojiDefaultStatuses,
        types.InputStickerSetEmojiDefaultTopicIcons,
        types.InputStickerSetEmojiGenericAnimations,
        types.InputStickerSetEmpty,
        types.InputStickerSetID,
        types.InputStickerSetPremiumGifts,
        types.InputStickerSetShortName
    ],
    pydantic.Field(discriminator='QUALNAME')
]
