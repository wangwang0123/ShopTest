import requests
from api.base_env import *


class OrderAPi:
    def __init__(self, token):
        self.url = test_env_config()['buyer']
        self.token = token

    def add_carts(self, data: dict):

        return requests.post(self.url + '/trade/carts', data=data, headers={'Authorization': self.token})

    def buy_now(self, json):
        return requests.post(self.url + '/trade/carts/buy', json=json, headers={'Authorization': self.token})

    def delete_cart(self):
        return requests.post(self.url + '/trade/carts', headers={'Authorization': self.token})


