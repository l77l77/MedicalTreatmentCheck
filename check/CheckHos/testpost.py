
import requests
import pandas as pd

#客户端
def http_post():
    url='http://api.quan9.club:8000/api'
    url2 = 'http://127.0.0.1:8000/api'
    f = open('./data_model/data/json.json', 'r')
    json_str_data = f.read()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    try:
        req = requests.post(url2,json_str_data,headers=headers)

    except requests.HTTPError as e:
        req = requests.post(url, json_str_data, headers=headers)

    # 生成页面请求的完整数据
         # 发送页面请求
    return req.text,req.status_code                # 获取服务器返回的页面信息

text,status=http_post()
print(text)