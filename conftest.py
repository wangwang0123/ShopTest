import requests
import uuid
import pytest

from api.base_env import test_env_config


@pytest.fixture(scope='session')
def buyer_login(params: dict):
    params['uuid'] = str(uuid.uuid4())
    return requests.post(test_env_config()['http']['buyer'] + '/passport/login', params=params)['access_token']