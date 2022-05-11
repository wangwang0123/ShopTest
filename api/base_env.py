

from common.file_load import *


def test_env_config(config_path='/config/http.yml'):
    return load_yaml_file(config_path)


if __name__ == "__main__":
    print(test_env_config()['buyer'])