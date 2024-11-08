import requests

from smart_airdrop_claimer import base
from core.headers import headers


def upgrade_character(data, token, proxies=None):
    url = "https://api.pitchtalk.app/v1/api/users/upgrade"

    try:
        response = requests.post(
            url=url,
            headers=headers(data=data, token=token),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        level = data["level"]
        coins = data["coins"]

        return level, coins
    except:
        return None, None


def process_upgrade_character(data, token, proxies=None):
    level, coins = upgrade_character(data=data, token=token, proxies=proxies)
    if level is not None:
        base.log(
            f"{base.white}Auto Upgrade Character: {base.green}Success {base.white}| {base.green}Coins: {base.white}{coins:,} - {base.green}Character Level: {base.white}{level}"
        )
    else:
        base.log(
            f"{base.white}Auto Upgrade Character: {base.red}Not enough coin to upgrade or Max available level reached"
        )


def upgrade_speed(data, token, proxies=None):
    url = "https://api.pitchtalk.app/v1/api/users/upgrade-speed"

    try:
        response = requests.post(
            url=url,
            headers=headers(data=data, token=token),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        speed_level = data["speedBoostLevel"]
        coins = data["coins"]

        return speed_level, coins
    except:
        return None, None


def process_upgrade_speed(data, token, proxies=None):
    speed_level, coins = upgrade_speed(data=data, token=token, proxies=proxies)
    if speed_level is not None:
        base.log(
            f"{base.white}Auto Upgrade Speed: {base.green}Success {base.white}| {base.green}Coins: {base.white}{coins:,} - {base.green}Speed Level: {base.white}{speed_level}"
        )
    else:
        base.log(
            f"{base.white}Auto Upgrade Speed: {base.red}Not enough coin to upgrade or Max available level reached"
        )
