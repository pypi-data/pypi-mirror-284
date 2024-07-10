import requests


def get_cf_token_v2():
    body = {
        "sitekey": "0x4AAAAAAAaHm6FnzyhhmePw",
        "url": "https://pioneer.particle.network/zh-CN/point",
        "invisible": False
    }
    r = requests.post("http://127.0.0.1:5555/solve", json=body)
    token = r.json()["token"]
    print("Solved :: " + token)
    return token

get_cf_token_v2()