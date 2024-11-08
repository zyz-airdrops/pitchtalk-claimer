import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_info(data, token, proxies=None):
    url = "https://api.pitchtalk.app/v1/api/users/me"

    try:
        response = requests.get(
            url=url,
            headers=headers(data=data, token=token),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        coins = data["coins"]
        tickets = data["tickets"]
        referral_rewards = data["referralRewards"]
        streak = data["loginStreak"]

        level = data["level"]
        speed_level = data["speedBoostLevel"]
        time_level = data["timeBoostLevel"]

        base.log(
            f"{base.green}Coins: {base.white}{coins:,} - {base.green}Tickets: {base.white}{tickets:,} - {base.green}Referral Rewards: {base.white}{referral_rewards} - {base.green}Streak: {base.white}{streak}"
        )
        base.log(
            f"{base.green}Character Level: {base.white}{level} - {base.green}Speed Level: {base.white}{speed_level} - {base.green}Time Level: {base.white}{time_level}"
        )
        return data
    except:
        return None
