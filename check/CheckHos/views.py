from django.shortcuts import render
from django.http import *
import json
import pandas as pd
from .read_json import json_to_list, lcovdf,lcovdf2
from .conculate_similarity import concluate_similarity
from .data_model import test_model

from django.views.decorators.csrf import csrf_exempt

from .cmp_item import cmp_item, dcode_to_dname
from .item_fx import item_conv


# ------数据库连接-------
host = '127.0.0.1'
port = 3306
user = 'root'
passwd = '123456'
db = 'huiqiao'
charset = 'utf8'


@csrf_exempt
def examine(request):
    if request.method == 'POST':
        try:
            rec= request.body.decode() #接受的数据
        except:
            msg = ('1post failed!')
            return HttpResponse(msg)
            # # rec_jdata =json.dumps({'list': [1, 0.02, 0.1, 14.27, 76.7, 16.9, 5.8, 0.3, 0.3, 10.95, 2.41, 0.83, 0.04, 0.04, 1.94, 61, 0.181, 93.3, 31.4, 337, 15.9, 201, 0.23, 11.3, 13.2, 5.02, 0.0974, 29, 12.2]})
        try:
           rec_ldata = json.loads(rec)
        except:
            msg = ('2post failed!')
            return HttpResponse(msg)
        try:
            rec_data = rec_ldata['list']
        except:
            msg = ('3post failed!')
            return HttpResponse(msg)

        df = lcovdf2(rec_data)
        # --多模型处理数据--
        vote = []
        try:
            predict1 = test_model.yucegbt2(df, training=False)
            vote.append(predict1[0])
        except:
            msg = "Model load fail errcode:-1"
            return HttpResponse(msg)
        try:
            predict2 = test_model.yucerf2(df, training=False)
            vote.append(predict2[0])
        except:
            msg = "Model load fail errcode:-2"
            return HttpResponse(msg)

        # try:
        #     predict3 = test_model.yucexgb2(df, training=False)
        #     vote.append(predict3[0])
        #
        # except:
        #     msg = "Model load fail errcode:-3"
        #     return HttpResponse(msg)
        finally:
            predict = pd.Series(vote)

        # --进行投票--
        try:
            # # #如果三个预测的值是相同的 就采用gbt的结果
            if predict2[0]==predict2[0]:
                y = predict2[0]
            else:
                y = 2
            return HttpResponse(y)
        except:
            msg = 'vote is errcode:-3'
            return HttpResponse(msg)
    else:
        # # #非POST请求
        context = str("111")
        return HttpResponse(context)


@csrf_exempt  # 取消防跨域请求
def api(request):
    if request.method == 'POST':

        # ----把json转换列表---
        try:
            data = json_to_list(request.body.decode(), False)
        except:
            # 如果无法成功转为list就在返回错误信息 msg
            msg = ('Post json type is errcode：-2')
            return HttpResponse(msg)

        # ----把数据转换成dataframe----
        # lcovdf() 将list 转换为 dataframe
        df = lcovdf(data)
        # 对 post 的数据有疑问看
        # 群里智能引擎测试接口说明文档 与 训练数据各字段说明
        patient_id = df['report_id'][0]

        # --多模型处理数据--
        vote = []
        try:
            predict1 = test_model.yucegbt(df, training=False)
            vote.append(predict1[0])
            predict2 = test_model.yucerf(df, training=False)
            vote.append(predict2[0])
            predict3 = test_model.yucexgb(df, training=False)
            vote.append(predict3[0])
            # thread1 = ThreadWithReturnValue(target=test_model.yucerf,
            #                                 args=(df,False))
            # thread2 = ThreadWithReturnValue(target=test_model.yucegbt,
            #                                 args=(df,False))
            # thread3 = ThreadWithReturnValue(target=test_model.yucexgb,
            #                         args=(df,False))
            # thread1.start()
            # thread2.start()
            # thread3.start()
            #
            # predict1= thread1.join()
            # vote.append(predict1[0])
            #
            # predict2 = thread2.join()
            # vote.append(predict2[0])
            #
            # predict3 = thread3.join()
            # vote.append(predict3[0])
        except:
            msg = "Model load fail errcode:-1"
            return HttpResponse(msg)
        finally:
            predict = pd.Series(vote)

        # --进行投票--
        try:
            # # #如果三个预测的值是相同的 就采用gbt的结果
            if predict.value_counts().values[0] == 3:
                y = predict1[0]
            else:
                y = 2
        except:
            msg = 'vote is errcode:-3'
            return HttpResponse(msg)
        # --计算相似度--
        # # #修改成前端运行（7.26)
        # y_pred = concluate_similarity(data, y, host, port, user, passwd, db, charset)
        msg = dict()
        msg['Report_id'] = str(patient_id)
        msg['Result'] = str(y)
        context = json.dumps(msg)
        return HttpResponse(context)
    else:
        # # #非POST请求
        context = str("111")
        return HttpResponse(context)


@csrf_exempt
def insert(request):
    if request.method == 'POST':  # 如果是post方法
        try:
            data = json_to_list(request.body, True)  # 解析jsonwen数据变成list
            print(len(data))
        except:
            msg = ('Post json type is error')
            return HttpResponse(msg)
        sql_insert = "INSERT INTO rbt_preprocessing01_0530 VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                     " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            row = (host, port, user, passwd, db, charset, sql_insert, tuple(data))
            msg = 'Data insert sucess!'
            print("effected rows:", row)
        except:
            msg = 'Data insert fail!'
    return HttpResponse(msg)


@csrf_exempt
def vtcheck(request):
    if request.method == 'POST':
        try:
            rec= request.body.decode() #接受的数据
        except:
            msg = ('1post failed!')
            return HttpResponse(msg)
            # # rec_jdata =json.dumps({'list': [1, 0.02, 0.1, 14.27, 76.7, 16.9, 5.8, 0.3, 0.3, 10.95, 2.41, 0.83, 0.04, 0.04, 1.94, 61, 0.181, 93.3, 31.4, 337, 15.9, 201, 0.23, 11.3, 13.2, 5.02, 0.0974, 29, 12.2]})
        try:
           rec_ldata = json.loads(rec)
        except:
            msg = ('2post failed!')
            return HttpResponse(msg)
        try:
            rec_data = rec_ldata['list']
        except:
            msg = ('3post failed!')
            return HttpResponse(msg)
        try:
            rec_list = item_conv(rec_data)
        except:
            msg = ('convert failed!')
            return HttpResponse(msg)
        try:
            d_return = cmp_item(rec_list)
        except:
            msg = ('cmp failed!')
            return HttpResponse(msg)

        d_code = d_return.diseases[0].get_code()
        res = dcode_to_dname(d_code)
        return HttpResponse(res)

@csrf_exempt
def cmp(request):
    if request.method == 'POST':
        try:
            rec = request.body.decode()  # 接受的数据
        except:
            msg = ('1post failed!')
            return HttpResponse(msg)
            # # rec_jdata =json.dumps({'list': [1, 0.02, 0.1, 14.27, 76.7, 16.9, 5.8, 0.3, 0.3, 10.95, 2.41, 0.83, 0.04, 0.04, 1.94, 61, 0.181, 93.3, 31.4, 337, 15.9, 201, 0.23, 11.3, 13.2, 5.02, 0.0974, 29, 12.2]})
        try:
            rec_ldata = json.loads(rec)
        except:
            msg = ('2post failed!')
            return HttpResponse(msg)
        try:
            rec_data = rec_ldata['list']
        except:
            msg = ('3post failed!')
            return HttpResponse(msg)
        try:
            rec_list = item_conv(rec_data)
        except:
            msg = ('convert failed!')
            return HttpResponse(msg)

        res = json.dumps(rec_list)
        return HttpResponse(res)