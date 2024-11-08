import requests
import random
import string

from smart_airdrop_claimer import base
from core.headers import headers
from core.info import get_info


def get_task(data, token, proxies=None):
    url = "https://api.pitchtalk.app/v1/api/tasks"

    try:
        response = requests.get(
            url=url,
            headers=headers(data=data, token=token),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()

        return data
    except:
        return None


def do_task(data, token, task_id, proxies=None):
    url = f"https://api.pitchtalk.app/v1/api/tasks/{task_id}/start"
    payload = {}

    try:
        response = requests.post(
            url=url,
            headers=headers(data=data, token=token),
            json=payload,
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        status = data["status"]

        return status
    except:
        return None


def verify(data, token, proxies=None):
    url = "https://api.pitchtalk.app/v1/api/tasks/verify"

    try:
        response = requests.get(
            url=url,
            headers=headers(data=data, token=token),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()

        return data
    except:
        return None


def process_do_task(data, token, proxies=None):
    task_list = get_task(data=data, token=token, proxies=proxies)
    for task in task_list:
        task_id = task["id"]
        task_status = task["status"]
        task_name = task["template"]["title"]

        if task_status == "COMPLETED_CLAIMED":
            base.log(f"{base.white}{task_name}: {base.green}Completed")
        else:
            do_task_status = do_task(
                data=data, token=token, task_id=task_id, proxies=proxies
            )
            verify_list = verify(data=data, token=token, proxies=proxies)
            verify_status = next(
                (item["status"] for item in verify_list if item["id"] == task_id),
                "Not found",
            )
            if verify_status == "COMPLETED_CLAIMED":
                base.log(
                    f"{base.white}{task_name}: {base.yellow}{do_task_status} -> {base.green}{verify_status}"
                )
            else:
                base.log(
                    f"{base.white}{task_name}: {base.yellow}{do_task_status} -> {base.red}{verify_status}"
                )


def claim_referral(data, token, proxies=None):
    url = "https://api.pitchtalk.app/v1/api/users/claim-referral"

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


def process_claim_ref(data, token, proxies=None):
    referral_rewards = get_info(data=data, token=token, proxies=proxies)[
        "referralRewards"
    ]
    if referral_rewards > 0:
        start_claim_ref = claim_referral(data=data, token=token, proxies=proxies)
        get_info(data=data, token=token, proxies=proxies)
    else:
        base.log(f"{base.white}Auto Claim Ref: {base.red}No point from ref")
