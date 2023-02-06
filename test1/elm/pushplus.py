import requests
import json


def push(title, content):
    token = '0ed33c48d001452387d7bbda84869d10'  # 在pushpush网站中可以找到

    url = 'http://www.pushplus.plus/send'
    data = {
        "token": token,
        "title": title,
        "content": content
    }
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    requests.post(url, data=body, headers=headers)
