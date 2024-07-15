from ExtraDecorators import validatetyping
from RTS_Twitch.toolset import paginate, single
from ExtraUtils.validate_dict import validate_dict

@validatetyping
async def get_broadcaster_subscriptions(channel_id:int,user_ids:list,first:int=20)->dict:
    '''[{
      "broadcaster_id": "141981764",
      "broadcaster_login": "twitchdev",
      "broadcaster_name": "TwitchDev",
      "gifter_id": "12826",
      "gifter_login": "twitch",
      "gifter_name": "Twitch",
      "is_gift": true,
      "tier": "1000",
      "plan_name": "Channel Subscription (twitchdev)",
      "user_id": "527115020",
      "user_name": "twitchgaming",
      "user_login": "twitchgaming"
    },
    ...
    ]'''
    url= f"https://api.twitch.tv/helix/subscriptions?broadcaster_id={channel_id}&first={first}"
    return await paginate(channel_id,url)

@validatetyping
async def test_subscription(channel_id:int,user_id:int)->dict:
    '''{
      "broadcaster_id": "149747285",
      "broadcaster_name": "TwitchPresents",
      "broadcaster_login": "twitchpresents",
      "is_gift": false,
      "tier": "1000"
    }'''
    url= f"https://api.twitch.tv/helix/subscriptions/user?broadcaster_id={channel_id}&user_id={user_id}"
    data = await single(channel_id,url)
    return data["data"]