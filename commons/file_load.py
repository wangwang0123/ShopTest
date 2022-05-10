# !/usr/bin python3
# encoding: utf-8 -*-
# @author: 汪亚亭

import yaml
from setting import DIR_NAME
import pandas


def load_excel(filepath, sheet_name):
    # keep_default_na 为false表示当你的单元格为空的时候，返回的是空字符串
    # engine表示选择的底层引擎是什么
    res = pandas.read_excel(DIR_NAME+filepath,sheet_name=sheet_name,keep_default_na=False,engine='openpyxl')
    # print(res)
    # 需要将拿到的数据转换成列表套列表的形式
    data = []  # 总的数据存储
    lines_count = res.shape[0]  # 表示从行数,不包括表头
    cols_count = res.shape[1]  # 表示总列数
    # print(lines_count,cols_count)
    for l in range(lines_count):
        lines = []
        for c in range(cols_count):
            cell_data = res.iloc[l, c]  # 获取单元格数据
            lines.append(cell_data)  # 将单元格数据追加lines这个列表里
        # 遍历列完成后，当前行的数据都存在lines中了
        data.append(lines)
    return data


def load_yaml_file(filepath):
    with open(DIR_NAME + filepath, mode='r', encoding='UTF-8') as f:
        yaml_content = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_content


def write_yaml(filepath, content):
    with open(DIR_NAME + filepath, mode='w', encoding='UTF-8') as f:
        yaml.dump(content, f, Dumper=yaml.Dumper)


if __name__ == '__main__':
    print(load_excel('/data/cart_testdata.xlsx', '添加购物车'))


