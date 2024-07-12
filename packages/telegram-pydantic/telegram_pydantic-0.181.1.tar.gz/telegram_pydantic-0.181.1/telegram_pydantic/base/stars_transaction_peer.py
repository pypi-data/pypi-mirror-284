from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StarsTransactionPeer - Layer 181
StarsTransactionPeer = typing.Annotated[
    typing.Union[
        types.StarsTransactionPeer,
        types.StarsTransactionPeerAppStore,
        types.StarsTransactionPeerFragment,
        types.StarsTransactionPeerPlayMarket,
        types.StarsTransactionPeerPremiumBot,
        types.StarsTransactionPeerUnsupported
    ],
    pydantic.Field(discriminator='QUALNAME')
]
