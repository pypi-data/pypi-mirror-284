from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MessageAction - Layer 181
MessageAction = typing.Annotated[
    typing.Union[
        types.MessageActionBoostApply,
        types.MessageActionBotAllowed,
        types.MessageActionChannelCreate,
        types.MessageActionChannelMigrateFrom,
        types.MessageActionChatAddUser,
        types.MessageActionChatCreate,
        types.MessageActionChatDeletePhoto,
        types.MessageActionChatDeleteUser,
        types.MessageActionChatEditPhoto,
        types.MessageActionChatEditTitle,
        types.MessageActionChatJoinedByLink,
        types.MessageActionChatJoinedByRequest,
        types.MessageActionChatMigrateTo,
        types.MessageActionContactSignUp,
        types.MessageActionCustomAction,
        types.MessageActionEmpty,
        types.MessageActionGameScore,
        types.MessageActionGeoProximityReached,
        types.MessageActionGiftCode,
        types.MessageActionGiftPremium,
        types.MessageActionGiveawayLaunch,
        types.MessageActionGiveawayResults,
        types.MessageActionGroupCall,
        types.MessageActionGroupCallScheduled,
        types.MessageActionHistoryClear,
        types.MessageActionInviteToGroupCall,
        types.MessageActionPaymentSent,
        types.MessageActionPaymentSentMe,
        types.MessageActionPhoneCall,
        types.MessageActionPinMessage,
        types.MessageActionRequestedPeer,
        types.MessageActionRequestedPeerSentMe,
        types.MessageActionScreenshotTaken,
        types.MessageActionSecureValuesSent,
        types.MessageActionSecureValuesSentMe,
        types.MessageActionSetChatTheme,
        types.MessageActionSetChatWallPaper,
        types.MessageActionSetMessagesTTL,
        types.MessageActionSuggestProfilePhoto,
        types.MessageActionTopicCreate,
        types.MessageActionTopicEdit,
        types.MessageActionWebViewDataSent,
        types.MessageActionWebViewDataSentMe
    ],
    pydantic.Field(discriminator='QUALNAME')
]
