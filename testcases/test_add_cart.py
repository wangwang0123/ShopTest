import pytest

import api.user_api
from api import user_api, order_api
from common.file_load import load_excel
import common.logger
import allure


class TestAddCart:

    logger = common.logger.GetLogger().get_logger()
    test_data = load_excel('/data/cart_testdata.xlsx', '添加购物车')
    @allure.story('添加购物车接口异常测试')
    @allure.title('{case_name}')
    @pytest.mark.parametrize('case_name,sku_id,num,expect_status_code,expect_business_code,expect_message', test_data)
    def test_add_cart(self, case_name, sku_id, num, expect_status_code, expect_business_code, expect_message):
        token = user_api.get_token({
            'username': 'shamo',
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'captcha': '1512'
        })
        self.logger.info('请求sku:{0},请求num：{1}'.format(sku_id, num))
        # commons.logger.GetLogger().get_logger().info('请求sku:{0},请求num：{1}'.format(sku_id, num))
        resp = order_api.OrderAPi(token=token).add_carts({'sku_id': sku_id, 'num': num})
        # print('res',resp.text)
        # resp = order_api.add_carts({'sku_id': sku_id, 'num': num}, token)
        status_code = resp.status_code
        assert status_code == expect_status_code
        print(resp.text)  # 由于响应信息可能为空，所以我们使用resp.text打印结果，因为空的字符串是无法使用resp.json()去获取的
        # 注意这个接口如果业务正常成功，那么响应信息是空的
        if status_code != 200:
            # 状态码不是200时，才进行响应信息的校验
            try:
                resp_json = resp.json()
            except:
                pass
            code = resp_json['code']
            # assert code == expect_busi_code

            pytest.assume(code == expect_business_code.replace('"', ''))
            # 判断message的值是 商品已失效，请刷新购物车
            message = resp_json['message']
            # assert message == expect_message
            pytest.assume(message == expect_message)


if __name__ == '__main__':
    pytest.main(['-vs'])
