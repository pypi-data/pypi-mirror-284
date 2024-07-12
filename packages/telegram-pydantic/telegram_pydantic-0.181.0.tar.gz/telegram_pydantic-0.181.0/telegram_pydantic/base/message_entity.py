from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MessageEntity - Layer 181
MessageEntity = typing.Annotated[
    typing.Union[
        types.InputMessageEntityMentionName,
        types.MessageEntityBankCard,
        types.MessageEntityBlockquote,
        types.MessageEntityBold,
        types.MessageEntityBotCommand,
        types.MessageEntityCashtag,
        types.MessageEntityCode,
        types.MessageEntityCustomEmoji,
        types.MessageEntityEmail,
        types.MessageEntityHashtag,
        types.MessageEntityItalic,
        types.MessageEntityMention,
        types.MessageEntityMentionName,
        types.MessageEntityPhone,
        types.MessageEntityPre,
        types.MessageEntitySpoiler,
        types.MessageEntityStrike,
        types.MessageEntityTextUrl,
        types.MessageEntityUnderline,
        types.MessageEntityUnknown,
        types.MessageEntityUrl
    ],
    pydantic.Field(discriminator='QUALNAME')
]
