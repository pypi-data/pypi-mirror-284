from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputPrivacyRule - Layer 181
InputPrivacyRule = typing.Annotated[
    typing.Union[
        types.InputPrivacyValueAllowAll,
        types.InputPrivacyValueAllowChatParticipants,
        types.InputPrivacyValueAllowCloseFriends,
        types.InputPrivacyValueAllowContacts,
        types.InputPrivacyValueAllowPremium,
        types.InputPrivacyValueAllowUsers,
        types.InputPrivacyValueDisallowAll,
        types.InputPrivacyValueDisallowChatParticipants,
        types.InputPrivacyValueDisallowContacts,
        types.InputPrivacyValueDisallowUsers
    ],
    pydantic.Field(discriminator='QUALNAME')
]
