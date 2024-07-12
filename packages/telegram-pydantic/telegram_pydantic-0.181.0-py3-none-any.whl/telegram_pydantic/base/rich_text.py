from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# RichText - Layer 181
RichText = typing.Annotated[
    typing.Union[
        types.TextAnchor,
        types.TextBold,
        types.TextConcat,
        types.TextEmail,
        types.TextEmpty,
        types.TextFixed,
        types.TextImage,
        types.TextItalic,
        types.TextMarked,
        types.TextPhone,
        types.TextPlain,
        types.TextStrike,
        types.TextSubscript,
        types.TextSuperscript,
        types.TextUnderline,
        types.TextUrl
    ],
    pydantic.Field(discriminator='QUALNAME')
]
