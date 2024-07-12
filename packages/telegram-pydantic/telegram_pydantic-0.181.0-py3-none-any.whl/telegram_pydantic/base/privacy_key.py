from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PrivacyKey - Layer 181
PrivacyKey = typing.Annotated[
    typing.Union[
        types.PrivacyKeyAbout,
        types.PrivacyKeyAddedByPhone,
        types.PrivacyKeyBirthday,
        types.PrivacyKeyChatInvite,
        types.PrivacyKeyForwards,
        types.PrivacyKeyPhoneCall,
        types.PrivacyKeyPhoneNumber,
        types.PrivacyKeyPhoneP2P,
        types.PrivacyKeyProfilePhoto,
        types.PrivacyKeyStatusTimestamp,
        types.PrivacyKeyVoiceMessages
    ],
    pydantic.Field(discriminator='QUALNAME')
]
