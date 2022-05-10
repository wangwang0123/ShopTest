# !/usr/bin python3
# encoding: utf-8 -*-
# @author: 汪亚亭
import json
import pymysql


class DBUtil:

    def __init__(self, host, user, password, port=3306):
        self.connect = pymysql.Connect(
            host=host,
            user=user,
            password=password,
            port=port,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def select(self, sql):
        cursor = self.connect.cursor()  # 相当于拿到了数据库数据集
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        self.connect.commit()  # 如果不提交数据，那么如果数据有更新，那么下次查询还是旧数据
        return data

    def update(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        self.connect.commit()
        cursor.close()

    def close(self):
        if self.connect is not None:
            self.connect.close()


if __name__ == '__main__':
    db_util = DBUtil(host='121.42.15.146', user='root', password='Testfan#123')
    # for i in range(10):
    #     time.sleep(10)
    #     data = db_util.select('SELECT * FROM mtxshop_trade.es_order WHERE member_id=59 ORDER BY order_id DESC LIMIT 1 ;')
    #     print(data[0])
    data = db_util.select('SELECT * FROM mtxshop_trade.es_order WHERE member_id=59 ORDER BY order_id ;')
    print("data",data)
    db_res = data[0]
    items_json = db_res['items_json']
    print(type(items_json))  # 由于items_json拿到之后是个字符串，不好从中提取内容
    # 所以我们可以将字符串转换列表套字典的形式
    # items_json = eval(items_json) # 这种不行，因为字符串有null，python里是None
    # print(type(items_json))
    items_json = json.loads(items_json)  # # 使用json库需要先导入import json
    print(type(items_json))
    print(items_json)
    print(items_json[0])
    print(items_json[0]['sku_id'])
    print(items_json[0]['num'])
    db_util.close()
