from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# phone.GroupCallStreamRtmpUrl - Layer 181
GroupCallStreamRtmpUrl = typing.Annotated[
    typing.Union[
        types.phone.GroupCallStreamRtmpUrl
    ],
    pydantic.Field(discriminator='QUALNAME')
]
