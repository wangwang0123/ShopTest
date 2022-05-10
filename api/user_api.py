import uuid

import requests
from api.base_env import *


def login(params: dict):
    params['uuid'] = str(uuid.uuid4())
    return requests.post(test_env_config()['http']['buyer'] + '/passport/login', params=params)


def get_token(params: dict):
    return login(params).json()['access_token']


print(login({
            'username': 'shamo',
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'captcha': '1512'
        }).json())