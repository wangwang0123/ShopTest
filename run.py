import sys

import pytest
import os
from common.file_load import load_yaml_file, write_yaml


if __name__ == '__main__':
    args = sys.argv
    env_file_path = '/config/env_test.yml'
    if len(args) > 1:
        env_name = args[1]  # 得到传入的环境名称
        env_file_path = f'/config/env_{env_name}.yml'  # 拼接环境配置文件路径
        del args[1]
        env_info = load_yaml_file(env_file_path)
        # 获取到环境信息之后，分别写http.yml,common.yml,redis.yml,db.yml
        write_yaml('/config/common.yml', env_info['common'])
        write_yaml('/config/http.yml', env_info['http'])
        write_yaml('/config/redis.yml', env_info['redis'])
        write_yaml('/config/db.yml', env_info['db'])
        # 执行时，会自动识别pytest.ini中的规则，完成执行
    pytest.main()
    os.system('allure generate ./report/data -o ./report/html --clean')