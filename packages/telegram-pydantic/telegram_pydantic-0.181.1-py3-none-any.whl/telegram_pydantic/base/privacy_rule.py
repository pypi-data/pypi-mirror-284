from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PrivacyRule - Layer 181
PrivacyRule = typing.Annotated[
    typing.Union[
        types.PrivacyValueAllowAll,
        types.PrivacyValueAllowChatParticipants,
        types.PrivacyValueAllowCloseFriends,
        types.PrivacyValueAllowContacts,
        types.PrivacyValueAllowPremium,
        types.PrivacyValueAllowUsers,
        types.PrivacyValueDisallowAll,
        types.PrivacyValueDisallowChatParticipants,
        types.PrivacyValueDisallowContacts,
        types.PrivacyValueDisallowUsers
    ],
    pydantic.Field(discriminator='QUALNAME')
]
