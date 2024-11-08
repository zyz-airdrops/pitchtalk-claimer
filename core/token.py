import requests
import json
from urllib.parse import parse_qs

from smart_airdrop_claimer import base
from core.headers import headers


parse_data = lambda data: {key: value[0] for key, value in parse_qs(data).items()}


def get_token(data, proxies=None):
    url = "https://api.pitchtalk.app/v1/api/auth"
    parser = parse_data(data)
    user = json.loads(parser["user"])
    payload = {
        "telegramId": str(user["id"]),
        "username": user["username"],
        "hash": data,
        "referralCode": "ffd116",
        "photoUrl": "",
    }

    try:
        response = requests.post(
            url=url,
            headers=headers(),
            json=payload,
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        token = data["accessToken"]
        return token
    except:
        return None
