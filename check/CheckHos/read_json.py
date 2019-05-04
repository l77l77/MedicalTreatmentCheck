# -*- coding: utf-8 -*-
"""
Created on Thu May 31 16:24:04 2018

@author: hq
目的: 获取json文件传过来的数据，用于构造传给模型的数据
******小知识*******
解析json文件，样例
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text = json.loads(jsonData)
"""
import json
import pandas as pd


#=================1.读取json字符串数据并且统一转换成列表list====================
def read_json(json_str,Isinsert=False):
    result_list = []
    data = json.loads(json_str) #多个对象，返回是list，单个对象返回是dict
    #if else 用于保证无论待解析的json是一个对象dict还是多个对象形成的列表list，都解析为list
    if type(data) is list:
        for item in data:
            new_item = parse_data(item,Isinsert) #返回结果为字典
            result_list.append(new_item) #转

            # 换为list
    else:
        new_item = parse_data(data,Isinsert)
        result_list.append(new_item)

    return result_list

#===============================2.解析数据=====================================
def parse_data(item,Isinsert):
    result_item = {}
    result_item["RepID"] = item.get("RepID",None) #item.get()指获取数据时，如果没有则为空None
    result_item["PatNO"] = item.get("PatNO",None)
    result_item["PatSex"] = item.get("PatSex",None)
    result_item["PatAge"] = item.get("PatAge",None)
    result_item["ItemID"] = item.get("ItemID",None)
    result_item["ItemCode"] = item.get("ItemCode",None)
    result_item["ItemResult"] = item.get("ItemResult",None)
    result_item["ItemUnit"] = item.get("ItemUnit",None)
    result_item["Date"] = item.get("Date",None)
    result_item["Diagnose"] = item.get("Diagnose", None)
    if Isinsert == True:
        result_item["y"] = item.get("y", None)
    return result_item

#=================3.根据解析json结果, 获取待审核的item_result===================
def get_result(p_data, Isinsert):
    item_id = ['11089', '11090', '2001', '2003', '2005', '2007', '2009', '2011',
                 '2013', '2015', '2017', '2019', '2021', '2023', '2025', '2027',
                 '2029', '2031', '2033', '2035', '2037', '2039', '2041', '2043',
                 '2051', '2053', '2056', '2062']
    item_id_fill = {'11089': '0', '11090': '0', '2001': '6.5', '2003': '57.5', '2005': '35',
                    '2007': '6.5', '2009': '4.2', '2011': '0.5', '2013': '4.05', '2015': '2.15',
                    '2017': '0.35', '2019': '0.27', '2021': '0.03', '2023': '4.45', '2025': '132.5',
                    '2027': '0.4', '2029': '91', '2031': '30.5', '2033': '335', '2035': '13',
                    '2037': '237.5', '2039': '0.25', '2041': '10.46', '2043': '13', '2051': '1.25',
                    '2053': '0.06', '2056': '6', '2062': '0.85'}
    item_result = []
    item_result.append(p_data[0]['PatNO'])
    item_result.append(p_data[0]['PatSex'])
    item_result.append(p_data[0]['PatAge'])
    item_result.append(p_data[0]['Diagnose'])
    item_result.append(p_data[0]['RepID'])
    item_result.append(p_data[0]['Date'])

    item = {}  #形如{'11090': '0', '11089': '0'}，共28项
    for i in range(len(p_data)):
        ItemID = p_data[i].get("ItemID", None)
        item[ItemID] = p_data[i].get("ItemResult", None)

    for itemid in item_id:
        try:
            item_result.append(float(item[itemid]))
        except:
            item_result.append(float(item_id_fill[itemid]))
    if Isinsert == True:
        item_result.append(p_data[0]['y'])
    return item_result

#==============================4.mian()=======================================
def json_to_list(p_json_str_data, Isinsert=False):
    data = read_json(p_json_str_data, Isinsert) #dict组成的列表，即[{...}, ...., {...}]  ###此时只有10（插入是11项）项值
    res = get_result(data, Isinsert)
    return res



#list转换成dataframe
def lcovdf(res):
    '''
    :param res:list,34个元素
    :return: dataframe
    '''
    #col：病人id,性别，年龄，诊断，报告单id,报告单日期
    col=['patient_id', 'sex', 'age', 'diagnose', 'report_id', 'report_date',
       'item_11089', 'item_11090', 'item_2001', 'item_2003',
       'item_2005', 'item_2007', 'item_2009', 'item_2011', 'item_2013',
       'item_2015', 'item_2017', 'item_2019', 'item_2021', 'item_2023',
       'item_2025', 'item_2027', 'item_2029', 'item_2031', 'item_2033',
       'item_2035', 'item_2037', 'item_2039', 'item_2041', 'item_2043',
       'item_2051', 'item_2053', 'item_2056', 'item_2062']
    # 将x,y转换为[x,y] 再变为字典
    res=dict(map(lambda x,y:[x,y],col,res))
    # res是一个报告单的数据结构
    data = pd.Series(res)
    data = pd.DataFrame(data).T
    # 将sex转换为int,此时data['sex']是Series类型 所以不能用int转换
    data['sex']=data['sex'].astype(int)
    col1=['item_11089', 'item_11090', 'item_2001', 'item_2003',
    'item_2005', 'item_2007', 'item_2009', 'item_2011', 'item_2013',
    'item_2015', 'item_2017', 'item_2019', 'item_2021', 'item_2023',
    'item_2025', 'item_2027', 'item_2029', 'item_2031', 'item_2033',
    'item_2035', 'item_2037', 'item_2039', 'item_2041', 'item_2043',
    'item_2051', 'item_2053', 'item_2056', 'item_2062']
    for i in col1:
        data[i]=data[i].astype(float)
    return data
    
def lcovdf2(res):
    '''
    :param res:list,34个元素
    :return: dataframe
    '''
    #col：病人id,性别，年龄，诊断，报告单id,报告单日期
    col=[ 'sex',
       'item_11089', 'item_11090', 'item_2001', 'item_2003',
       'item_2005', 'item_2007', 'item_2009', 'item_2011', 'item_2013',
       'item_2015', 'item_2017', 'item_2019', 'item_2021', 'item_2023',
       'item_2025', 'item_2027', 'item_2029', 'item_2031', 'item_2033',
       'item_2035', 'item_2037', 'item_2039', 'item_2041', 'item_2043',
       'item_2051', 'item_2053', 'item_2056', 'item_2062']
    # 将x,y转换为[x,y] 再变为字典
    res=dict(map(lambda x,y:[x,y],col,res))
    # res是一个报告单的数据结构
    data = pd.Series(res)
    data = pd.DataFrame(data).T
    # 将sex转换为int,此时data['sex']是Series类型 所以不能用int转换
    data['sex']=data['sex'].astype(int)
    col1=['item_11089', 'item_11090', 'item_2001', 'item_2003',
    'item_2005', 'item_2007', 'item_2009', 'item_2011', 'item_2013',
    'item_2015', 'item_2017', 'item_2019', 'item_2021', 'item_2023',
    'item_2025', 'item_2027', 'item_2029', 'item_2031', 'item_2033',
    'item_2035', 'item_2037', 'item_2039', 'item_2041', 'item_2043',
    'item_2051', 'item_2053', 'item_2056', 'item_2062']
    for i in col1:
        data[i]=data[i].astype(float)
    return data
# f = open('json.json', 'r')
# json_str_data = f.read()#整个文件作为一个字符串，即[{...}, ...., {...}]
# result = main(json_str_data)










