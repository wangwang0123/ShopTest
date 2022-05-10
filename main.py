import pytest
import os

pytest.main()


os.system('allure generate ./report/data -o ./report/html --clean')