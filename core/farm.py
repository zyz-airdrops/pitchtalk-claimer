import requests
from datetime import datetime, timezone

from smart_airdrop_claimer import base
from core.headers import headers


def farmings(data, token, proxies=None):
    url = "https://api.pitchtalk.app/v1/api/farmings"

    try:
        response = requests.get(
            url=url,
            headers=headers(data=data, token=token),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        end_time = data["endTime"]

        return end_time
    except:
        return None


def create_farming(data, token, proxies=None):
    url = "https://api.pitchtalk.app/v1/api/users/create-farming"

    try:
        response = requests.post(
            url=url,
            headers=headers(data=data, token=token),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        end_time = data["farming"]["endTime"]

        return end_time
    except:
        return None


def claim_farming(data, token, proxies=None):
    url = "https://api.pitchtalk.app/v1/api/users/claim-farming"

    try:
        response = requests.post(
            url=url,
            headers=headers(data=data, token=token),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()

        return data
    except:
        return None


def process_farming(data, token, proxies=None):
    try:
        end_time = farmings(data=data, token=token, proxies=proxies)
        if end_time:
            formatted_end_time = datetime.strptime(
                end_time, "%Y-%m-%dT%H:%M:%S.%fZ"
            ).replace(tzinfo=timezone.utc)
            current_utc = datetime.now(timezone.utc)
            if formatted_end_time > current_utc:
                base.log(f"{base.white}Auto Farm: {base.red}Not time to claim yet")
                base.log(
                    f"{base.white}Auto Farm: {base.yellow}End at {formatted_end_time} (UTC)"
                )
            else:
                base.log(f"{base.white}Auto Farm: {base.yellow}Claiming...")
                start_claim_farming = claim_farming(
                    data=data, token=token, proxies=proxies
                )
        else:
            base.log(f"{base.white}Auto Farm: {base.yellow}Starting farming...")
            end_time_cre = create_farming(data=data, token=token, proxies=proxies)
            formatted_end_time_cre = datetime.strptime(
                end_time_cre, "%Y-%m-%dT%H:%M:%S.%fZ"
            ).replace(tzinfo=timezone.utc)
            base.log(
                f"{base.white}Auto Farm: {base.yellow}End at {formatted_end_time_cre} (UTC)"
            )
    except Exception as e:
        base.log(f"{base.white}Auto Farm: {base.red}Error - {e}")
