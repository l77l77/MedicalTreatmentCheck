# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:53:31 2018

@author: hq
功能: 根据patient_id查找数据库lxz中表RBT_preprocessing01_0530最近的一条数据，计算相似度
"""

import pymysql



def insert_DB(host, port, user, passwd, db, charset, p_sql_insert, p_res_list):
    # 创建连接
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    # 创建游标
    cur = conn.cursor()
    # 执行SQL，并返回收影响行数
    effect_row = cur.execute(p_sql_insert, p_res_list)
    conn.commit()
    cur.close()
    conn.close()
    return effect_row


# ===================1.连接数据库，获取历史数据===========================
def read_DB(p_host, p_port, p_user, p_passwd, p_db, p_charset, p_sql_read):
    conn = pymysql.connect(host=p_host, port=p_port, user=p_user, passwd=p_passwd,
                           db=p_db, charset=p_charset)
    cur = conn.cursor()
    count_row = cur.execute(p_sql_read)
    content = cur.fetchall()
    cur.close()
    conn.close()
    return content


# ======================2.计算item[]与old_item[]差值百分比======================
"""
p_json: json文件的内容
p_y: 模型预测的结果
"""


def concluate_similarity(p_json, p_y, p_host, p_port, p_user, p_passwd, p_db, p_charset):
    # 读取数据库数据
    patient_id = p_json[0]
    try:
        sql_read = "select * from RBT_preprocessing01_0530 where patient_id = %s order by report_date desc limit 1" % (
            patient_id)
        # # # 此时的past_data 是一个conn对象
        past_data = read_DB(p_host, p_port, p_user, p_passwd, p_db, p_charset, sql_read)
        print(past_data)
        if past_data == ():
            item_id_fill = ['0', '0', '6.5', '57.5', '35', '6.5', '4.2', '0.5', '4.05', '2.15',
                            '0.35', '0.27', '0.03', '4.45', '132.5', '0.4', '91', '30.5', '335',
                            '13', '237.5', '0.25', '10.46', '13', '1.25', '0.06', '6', '0.85']
            item_new = p_json[6:-1]

            if item_new[0] > 4 or item_new[1] > 4:
                return 1
            for i in range(2, len(item_new)):  # 28
                ratio = abs(float(item_new[i]) - float(item_id_fill[i])) / float(item_id_fill[i])
                if ratio > 2:
                    return 1
            return p_y
    except:
        msg = 'sql connect error'
        return (msg)

    past_data = past_data[0]  # len=34
    # 先判断历史记录标签和模型预测的p_y是否相同，不同则直
    # 相同则取历史28项
    item_old = []
    item_new = p_json[6:-1]  # len(p_json)=34, len(item_new)=28
    for i in range(6, len(p_json)):  # 从s[6]开始item_10089,共28项，到6+28-1=33结束
        item_old.append(float(past_data[i]))
    # 计算每个项目相似度
    cou = 0
    for i in range(len(item_new)):  # 28
        maxnium = max(item_new[i], item_old[i])
        minnium = min(item_new[i], item_old[i])
        if maxnium == 0:
            cou += 1
        else:
            ratio = abs(item_new[i] - item_old[i]) / (minnium + 0.0001)
            if ratio < 0.1:
                cou += 1

    # 计算2条记录相似度
    if cou == (len(item_new)):
        y_pred = past_data[len(past_data) - 1]
    else:
        y_pred = 2  # 不相似，可疑
    # 下结论
    if int(y_pred) == int(p_y):
        print(y_pred)
        return p_y
    else:
        return 2  # 可疑数据

#
# host='127.0.0.1'
# port=3306
# user='root'
# passwd='123456'
# db='huiqiao'
# charset='utf8'
# f = open('./data_model/data/json.json', 'r')
# json_str_data = f.read()#整个文件作为一个字符串，即[{...}, ...., {...}]
# result = json_to_list(json_str_data, True)
# print(result)
# y_model = 1
#
# #y_pred = concluate_similarity(result, y_model, host, port, user, passwd, db, charset)
# #print(y_pred)
# sql_insert = "INSERT INTO rbt_preprocessing01_0530 VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
#              " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# insert_DB(host, port, user, passwd, db, charset, sql_insert, tuple(result))
