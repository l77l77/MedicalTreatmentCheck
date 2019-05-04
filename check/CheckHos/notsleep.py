
from CheckHos.read_json import json_to_list, lcovdf,lcovdf2
from CheckHos.data_model import test_model


data = [1,0.02,0.1,14.27,76.7,16.9,5.8,0.3,0.3,10.95,2.41,0.83,
            0.04,0.04,1.94,61,0.181,93.3,31.4,337,15.9,201,0.23,11.3,
            13.2,5.02,0.0974,29,12.2]

df = lcovdf2(data)
# --多模型处理数据--
vote = []
try:
   # predict1 = test_model.yucegbt2(df, training=False)
   # print(predict1)
   # predict2 = test_model.yucerf2(df, training=False)
   # print(predict2)
   # vote.append(predict2[0])
   predict3 = test_model.yucexgb2(df, training=False)
   print(predict3)
#    vote.append(predict3[0])
except:
   msg = "Model load fail errcode:-1"
   print(msg)

# --进行投票--
# try:
#    # # #如果三个预测的值是相同的 就采用gbt的结果
#    if predict.value_counts().values[0] == 3:
#       y = predict1[0]
#    else:
#       y = 2
#       print(msg)
# except:
#    msg = 'vote is errcode:-3'
#    print(msg)