from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# TopPeerCategoryPeers - Layer 181
TopPeerCategoryPeers = typing.Annotated[
    typing.Union[
        types.TopPeerCategoryPeers
    ],
    pydantic.Field(discriminator='QUALNAME')
]
