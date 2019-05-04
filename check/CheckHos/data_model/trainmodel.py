import numpy as np
import pandas as pd
from sklearn import cross_validation
from imblearn.over_sampling import SMOTE
# from xgboost.sklearn import XGBClassifier
# import xgboost as xgb
from sklearn import cross_validation, metrics
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import IsolationForest
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn import metrics
import os

#定义模型１即训练模型
class models(object):
    def __init__(self):
        pass
    def clean_data(self,data):
        try:
            data = data[data['rank'] == 1]
        except:
            msg="没有rank字段"
            # print("没有rank字段！")
        finally:
            data['age1'] = data['age'].apply(lambda x: str(x).split('Y')[0])
            data['month'] = data['age'].apply(lambda x: str(x).split('Y')[1].split('M')[0])
            data['day'] = data['age'].apply(lambda x: str(x).split('Y')[1].split('M')[1].split('D')[0])
            data['age0'] = data['age'].apply(dealage)

        col = ['sex',
           'item_11089', 'item_11090', 'item_2001', 'item_2003',
           'item_2005', 'item_2007', 'item_2009', 'item_2011', 'item_2013',
           'item_2015', 'item_2017', 'item_2019', 'item_2021', 'item_2023',
           'item_2025', 'item_2027', 'item_2029', 'item_2031', 'item_2033',
           'item_2035', 'item_2037', 'item_2039', 'item_2041', 'item_2043',
           'item_2051', 'item_2053', 'item_2056', 'item_2062',  'age0']
        try:
            label = data[['y']]
        except:
            data=data[col]
            return data
        else:
            data=data[col]

        return data,label

    def clean_data2(self, data):
        data['age0'] = 4
        col = ['sex',
               'item_11089', 'item_11090', 'item_2001', 'item_2003',
               'item_2005', 'item_2007', 'item_2009', 'item_2011', 'item_2013',
               'item_2015', 'item_2017', 'item_2019', 'item_2021', 'item_2023',
               'item_2025', 'item_2027', 'item_2029', 'item_2031', 'item_2033',
               'item_2035', 'item_2037', 'item_2039', 'item_2041', 'item_2043',
               'item_2051', 'item_2053', 'item_2056', 'item_2062','age0']
        try:
            label = data[['y']]
        except:
            data = data[col]
            return data
        else:
            data = data[col]

        return data, label
    #分个数据集
    def split_data(self,data,label):
        features_train, features_test, labels_train, labels_test =cross_validation.train_test_split(data,
                                                                            label,
                                                                            test_size=0.3,random_state=0)
        return features_train, features_test, labels_train, labels_test
        #对数据进行过采样
    def oversample(self,features_train,labels_train):
        oversampler = SMOTE(random_state=0)
        os_features, os_labels = oversampler.fit_sample(features_train, labels_train)
        return os_features,os_labels

    #训练模型
    def modelfit(self,alg, dtrain, dtrainlabel, dtest, dtestlabel):
        # '''
        # alg 表示的是分类器　dtrain表示的训练集,dtrainlaebel表示的训练集的标签　dtest表示的测试集  dtestlael表示预测集的label
        # '''

        # 训练
        alg.fit(dtrain, dtrainlabel)

        # 对训练集预测
        dtrain_predictions = alg.predict(dtrain)
        dtrain_predprob = alg.predict_proba(dtrain)[:, 1]
        # 对测试集预测
        dtest_predictions = alg.predict(dtest)
        dtest_predprob = alg.predict_proba(dtest)[:, 1]


        print("\n关于现在这个模型")
        print("训练集准确率 : %.4g" % metrics.accuracy_score(dtrainlabel.values, dtrain_predictions))
        print("AUC 训练集得分 (训练集): %f" % metrics.roc_auc_score(dtrainlabel, dtrain_predprob))


        print('打印出测试集分类报告')
        target_names = ['class0', 'class1']
        print(metrics.classification_report(dtestlabel.values, dtest_predictions, target_names=target_names))

        return alg

class model2(models):
    def __init__(self):
        super(model2,self).__init__()
    def Clustering(self,data,label):
        clf = IsolationForest(n_estimators=100, max_samples=200, n_jobs=-1)
        clf.fit(data)
        scores_pred = clf.decision_function(data)
        data['scores'] = scores_pred
        data['y']=label
        data = data.drop(data.loc[((data['y'] == 1) & (0.13 < data['scores']))].index)
        data = data.drop(data.loc[((data['y'] == 1) & (data['scores'] < -0.13))].index)
        data = data.drop(data.loc[((data['y'] == 0) & (data['scores'] < 0))].index)
        data = data.drop(data.loc[((data['y'] == 0) & (data['scores'] > 0.15))].index)
        label = data[['y']]
        del data['scores']
        del data['y']
        return data,label
    #-------对数据进行分箱
    def fenxiang(self,data):
        b = ['item_11089', 'item_11090', 'item_2001', 'item_2003', 'item_2005', 'item_2007', 'item_2009', 'item_2011',
             'item_2013', 'item_2015', 'item_2017', 'item_2019', 'item_2021', 'item_2023', 'item_2025', 'item_2027',
             'item_2029', 'item_2031', 'item_2033', 'item_2035', 'item_2037', 'item_2039', 'item_2041', 'item_2043',
             'item_2051', 'item_2053', 'item_2056', 'item_2062']
        # for i in b:
        #     data[i] = data[i].astype(float)
        data['item_11089'] = data['item_11089'].apply(delitem_11089_11090)
        data['item_11090'] = data['item_11090'].apply(delitem_11089_11090)
        data['item_2001'] = data['item_2001'].apply(delitem_2001)
        data['item_2009'] = data['item_2009'].apply(delitem_2009)
        data['item_2013'] = data['item_2013'].apply(delitem_2013)
        data['item_2015'] = data['item_2015'].apply(delitem_2015)
        data['item_2017'] = data['item_2017'].apply(delitem_2017)
        data['item_2019'] = data['item_2019'].apply(delitem_2019)
        data['item_2021'] = data['item_2021'].apply(delitem_2021)
        data['item_2029'] = data['item_2029'].apply(delitem_2029)
        data['item_2031'] = data['item_2031'].apply(delitem_2031)
        data['item_2033'] = data['item_2033'].apply(delitem_2033)
        data['item_2035'] = data['item_2035'].apply(delitem_2035)
        data['item_2037'] = data['item_2037'].apply(delitem_2037)
        data['item_2039'] = data['item_2039'].apply(delitem_2039)
        data['item_2041'] = data['item_2041'].apply(delitem_2041)
        data['item_2043'] = data['item_2043'].apply(delitem_2043)
        data['item_2053'] = data['item_2053'].apply(delitem_2053)
        data['item_2056'] = data['item_2056'].apply(delitem_2056)
        data['item_2062'] = data['item_2062'].apply(delitem_2062)
        data['item_2003'] = data['item_2003'].apply(item_2003)
        data['item_2005'] = data['item_2005'].apply(item_2005)
        data['item_2007'] = data['item_2007'].apply(item_2007)
        data['item_2011'] = data['item_2011'].apply(item_2011)
        data['item_2051'] = data['item_2051'].apply(item_2051)
        data['item_2023'] = data['item_2023'].apply(item_2023)
        data['item_2025'] = data['item_2025'].apply(item_2025)
        data['item_2027'] = data['item_2027'].apply(item_2005)
        del data['sex']
        del data['age0']
        return data
    #特征组合
    def feature_cross(self,data,label,fag=True):

        if fag==True:
            n_estimator = 100
        else:
            n_estimator = 28
        # GBDT
        grd = GradientBoostingClassifier(n_estimators=n_estimator)
        # one-hot类实例化
        # 放入当GBDT中训练

        grd.fit(data.values, label.values)
        joblib.dump(grd,'./model/gbtt.pkl')
        if fag == True:
            joblib.dump(grd,'./model/gbt.pkl')
        return grd


    #产生新的特征并onehot化
    # def loadmodel(self,flag=True):
    #     '''
    #
    #     :param flag:bool类型　表示是否测试
    #     :return:
    #     '''
    #     if flag==True:
    #         grd=joblib.load('./model/gbtt.pkl')
    #     else:
    #         current_path = os.getcwd()
    #         pklpath = current_path + '/Check/data_model//model/gbtt.pkl'
    #         grd=joblib.load(pklpath)
    #     return grd


    # def gentorfeaure(self,grd,data):
    #     grd_enc = OneHotEncoder()
    #     # print(data.info())
    #     grd_enc.fit(grd.apply(data)[:, :, 0])
    #     return grd_enc,grd



    # def fitmodel(self,data,label):
    #     xgb1 = XGBClassifier(
    #         booster='gbtree',
    #         learning_rate=0.1,
    #         n_estimators=1000,
    #         max_depth=6,
    #         min_child_weight=3,
    #         gamma=0.2,
    #         subsample=0.9,
    #         colsample_bytree=0.9,
    #         objective='binary:logistic',
    #         nthread=4,
    #         scale_pos_weight=1,
    #         seed=27)
    #     # 找到最有的分类器个数
    #     xgb_param = xgb1.get_xgb_params()  # 得到分类器的配置参数
    #     xgtrain = xgb.DMatrix(data,
    #                           label=label['y'].values)  # 对训练集进行矩阵化
    #
    #     cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=xgb1.get_params()['n_estimators'], nfold=5,
    #                       early_stopping_rounds=300, show_stdv=True)  # 进行五折交叉验证得到，得到效果最好的时候用多少个分类器
    #
    #     xgb1.set_params(n_estimators=cvresult.shape[0])
    #
    #     xgb1.fit(data, label.values)
    #     joblib.dump(xgb1, './model/xgb1.pkl')

#对年龄进行分段
def dealage(x):
    age = int(x.split('Y')[0])
    if age >= 6:
        x = 4
    elif 1 <= age < 6:
        x = 3
    elif age < 1:
        month = int(x.split('Y')[1].split('M')[0])
        if month > 0:
            x = 2
        else:
            x = 1
    return x

#－－－－－－定义分箱－－－－－－－－

def delitem_11089_11090(x):
    if x == 0:
        x = 0
    else:
        x = 1
    return x


def delitem_2001(x):
    if 3.5 <= x <= 9.5:
        x = 0
    elif x < 1:
        x = 2
    else:
        x = 1
    return x


def delitem_2009(x):
    if 0.4 <= x <= 8:
        x = 0
    else:
        x = 1
    return x


def delitem_2013(x):
    if 1.8 <= x <= 6.3:
        x = 0
    else:
        x = 1
    return x


def delitem_2015(x):
    if 1.1 <= x < 3.2:
        x = 0
    else:
        x = 1
    return x


def delitem_2017(x):
    if 0.1 <= x <= 0.6:
        x = 0
    else:
        x = 1
    return x


def delitem_2019(x):
    if 0.02 <= x <= 0.52:
        x = 0
    else:
        x = 1
    return x


def delitem_2021(x):
    if 0 <= x <= 0.06:
        x = 0
    else:
        x = 1
    return x


def delitem_2029(x):
    if 82 <= x <= 100:
        x = 0
    else:
        x = 1
    return x


def delitem_2031(x):
    if 27 <= x <= 34:
        x = 0
    else:
        x = 1
    return x


def delitem_2033(x):
    if 316 <= x <= 354:
        x = 0
    else:
        x = 1
    return x


def delitem_2035(x):
    if 11.5 <= x <= 14.5:
        x = 0
    else:
        x = 1
    return x


def delitem_2037(x):
    if 125 <= x <= 350:
        x = 0
    elif x <= 20:
        x = 2
    else:
        x = 1
    return x


def delitem_2039(x):
    if 0.11 <= x <= 0.39:
        x = 0
    else:
        x = 1
    return x


def delitem_2041(x):
    if 7.66 <= x <= 13.26:
        x = 0
    else:
        x = 1
    return x


def delitem_2043(x):
    if 9 <= x <= 17:
        x = 0
    else:
        x = 1
    return x


def delitem_2053(x):
    if 0.02 <= x <= 0.1:
        x = 0
    else:
        x = 1
    return x


def delitem_2056(x):
    if 1.6 <= x <= 10.5:
        x = 0
    else:
        x = 1
    return x


def delitem_2062(x):
    if 0 <= x <= 1.7:
        x = 0
    else:
        x = 1
    return x

#对年龄
def age_item_2003(age,item):

    if age==1|age==2:
        if 31<=item<=40:
            return 0
        else:
            return 1
    elif age==3:
        if 50<=item<70:
            return 0
        else:
            return 1
    else:
        if 40<=item<=75:
            return 0
        else:
            return 1
def item_2003(item):
    if 31<=item<=70:
        return 0
    else:
        return 1
#对年龄
def age_item_2005(age,item):
    if age==1|age==2:
        if 40<=item<=60:
            return 0
        else:
            return 1
    elif age==3:
        if 20<=item<40:
            return 0
        else:
            return 1
    else:
        if 20<=item<=50:
            return 0
        else:
            return 1

def item_2005(item):
   if 20<=item<=50:
       return 0
   else:return 1

#对年龄
def age_item_2007(age,item):
    if age==1:
        if 1<=item<=12:
            return 0
        else:
            return 1
    elif age==3|age==2:
        if 1<=item<8:
            return 0
        else:
            return 1
    else:
        if 3<=item<=10:
            return 0
        else:
            return 1

def item_2007(item):
    if 3<=item<=18:
        return 0
    else:
        return 1
#这里可以最优数来编程
#对年龄
def age_item_2011(age,item):
    if age==1|age==3|age==2:
        if 0<=item<=7:
            return 0
        else:
            return 1
    else:
        if 0<=item<=1:
            return 0
        else:
            return 1
def item_2011(item):
    if 0<=item<=7:
        return 0
    else:return 1

#对年龄
def age_item_2051(age,item):
    if age==1:
        if 3<=item<=6:
            return 0
        else:
            return 1
    else:
        if 0.5<=item<=2:
            return 0
        else:
            return 1
def item_2051(item):
    if 0.5<=item<=1:
        return 0
    else:return 1

def sex_age_item2023(sex,age,item):
    if sex==2&age==4:
        if 3.8<=item<=5.1:
            return 0
        else :
            return 1
    elif sex==1&age==4:
        if 4.3<=item<=5.8:
             return 0
        else:
             return 1
    elif age==1:
        if 5.2<=item<=6.4:
            return 0
        else:
            return 1
    else:
        if 4<=item<=4.5:
            return 0
        else:
            return 1
def item_2023(item):
    if 4 <= item <= 4.5:
        return 0
    else:
        return 1


def sex_age_item2025(sex,age,item):
    if sex==2&age==4:
        if 115<=item<=150:
            return 0
        elif item<50:
            return 2
        else :
            return 1
    elif sex==1&age==4:
        if 130<=item<=175:
             return 0
        elif item<50:
            return 2
        else:
             return 1
    elif age==1:
        if 180<=item<=190:
            return 0
        elif item<50:
            return 2
        else:
            return 1
    else:
        if 120<=item<=140:
            return 0
        elif item<50:
            return 2
        else:
            return 1

def item_2025(item):
    if 120 <= item <= 140:
        return 0
    else:return 1

def delitem_2027(sex,x):
    if sex==1:
        if 0.4<=x<=0.5:
            x=0
        else:
            x=1
    else :
        if  0.35<=x<=0.45:
            x=0
        else:
            x=1
    return x

def item_2027(item):
    if 0.35 <= x <= 0.45:
        x = 0
    else:
        x = 1

def train_model_rf():
    data = pd.read_csv('./data/train.csv')
    model1 = models()
    data, label = model1.clean_data(data)

    features_train, features_test, labels_train, labels_test = model1.split_data(data, label)

    os_features, os_labels = model1.oversample(features_train, labels_train)

    os_features = pd.DataFrame(os_features)
    os_labels = pd.DataFrame(os_labels)
    os_features.columns = features_test.columns
    os_labels.columns = labels_test.columns

    rf = RandomForestClassifier(random_state=0, n_estimators=200, n_jobs=-1)

    alg = model1.modelfit(rf, os_features, os_labels, features_test, labels_test)
    joblib.dump(alg, './model/rf01.pkl')


if __name__ == '__main__':
    data = pd.read_csv('./data/train.csv')
    model3=model2()#实列化方法
    data,label = super(model2,model3).clean_data(data)
    data,label=model3.Clustering(data,label)
    features_train, features_test, labels_train, labels_test=super(model2, model3).split_data(data,label)
    os_features,os_labels = super(model2,model3).oversample(features_train,labels_train)
    os_features = pd.DataFrame(os_features)
    os_labels = pd.DataFrame(os_labels)
    os_features.columns = features_test.columns
    os_labels.columns = labels_test.columns
    train_X=model3.fenxiang(os_features)

    test_X=model3.fenxiang(features_test)
    # grd=model3.feature_cross(train_X,os_labels,fag=False)#特征交叉
    # grd_enc,grd=model3.gentorfeaure(grd,train_X)
    # model3.fitmodel(train_X,os_labels)