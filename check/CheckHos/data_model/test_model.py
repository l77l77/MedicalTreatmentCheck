import pandas as pd
from django.http import HttpResponse
from sklearn.externals import joblib
from .trainmodel import models,model2
# from Checkhos.Check.data_model.trainmodel import models,model2

import os

#-------使用随机森林预测--------
#如果做api调用的话需要把clean_data2改为clean_data
def yucerf(test,training=True):

    model1=models()
    if training==True:
        test,label = model1.clean_data(test) #预处理数据
    else:
        test = model1.clean_data(test)
    current_path = os.getcwd()
    pklpath = current_path + '/CheckHos/data_model/model/rf01.pkl'
    alg = joblib.load(pklpath)
    prediction = alg.predict(test)


    return prediction

#-------使用xgboost－－－－－－－
def yucexgb(test,training=True):
    '''

    :param test: Dataframe类型,
    :param training: bool类型表示本地是否
    :return:
    '''
    model3=model2()
    #对数据进行清洗获取想要的字段
    if training==True:
        data,label=super(model2,model3).clean_data(test)
    else:
        data=super(model2,model3).clean_data(test)

    train_X = model3.fenxiang(data)

    if training==True:
        alg=joblib.load('./model/xgb1.pkl')
        prediction=alg.predict(train_X)
    else:
        current_path = os.getcwd()
        pklpath = current_path + '/CheckHos/data_model/model/xgb1.pkl'
        alg = joblib.load(pklpath)
        prediction = alg.predict(train_X)

    return prediction

#-------使用GBDT预测－－－－－－
def yucegbt(test,training=True):
    model3=model2()
    if training==True:
        data,label=super(model2,model3).clean_data(test)
    else:
        data=super(model2,model3).clean_data(test)
    train_X = model3.fenxiang(data)

    current_path = os.getcwd()
    pklpath = current_path + '/CheckHos/data_model/model/gbt.pkl'

    alg = joblib.load(pklpath)
    prediction = alg.predict(train_X)

    return prediction

def yucegbt2(test,training=True):
    model3=model2()
    if training==True:
        data,label=super(model2,model3).clean_data(test)
    else:
        data=super(model2,model3).clean_data2(test)
    train_X = model3.fenxiang(data)

    current_path = os.getcwd()
    pklpath = current_path + '/CheckHos/data_model/model/gbt.pkl'

    alg = joblib.load(pklpath)
    # print(train_X)
    prediction = alg.predict(train_X)

    return prediction

def yucerf2(test,training=True):

    model1=models()
    if training==True:
        test,label = model1.clean_data2(test) #预处理数据
    else:
        test = model1.clean_data2(test)
        # print(test)
    current_path = os.getcwd()
    pklpath = current_path + '/CheckHos/data_model/model/rf01.pkl'
    alg = joblib.load(pklpath)
    prediction = alg.predict(test)


    return prediction

def yucexgb2(test,training=True):
    '''

    :param test: Dataframe类型,
    :param training: bool类型表示本地是否
    :return:
    '''
    model3=model2()
    #对数据进行清洗获取想要的字段
    if training==True:
        data,label=super(model2,model3).clean_data(test)
    else:
        data=super(model2,model3).clean_data2(test)

    train_X = model3.fenxiang(data)
    # print(train_X)
    if training==True:
        alg=joblib.load('./model/xgb1.pkl')
        prediction=alg.predict(train_X)
    else:
        try:
            current_path = os.getcwd()
            pklpath = current_path + '/CheckHos/data_model/model/xgb1.pkl'
            alg = joblib.load(pklpath)
        except:
            msg='path error'
        try:
            prediction = alg.predict(train_X)
        except:
            msg='alg error'
    return msg

if __name__ =='__main__':

    data = pd.read_csv('./data/train.csv')
    # print(data.head(1))
    prediction=yucerf(data)

