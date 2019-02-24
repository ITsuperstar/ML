# encoding=utf-8
import datetime
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
# 数据分析，朴素贝叶斯
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from scipy.sparse.csr import csr_matrix
from scipy import sparse
from sklearn.svm import SVC

# 读取数据
data = pd.read_csv("fword-all.csv", encoding='utf-8')
'''
# 取内容
X = (data.iloc[:, :-1]).values
X=csr_matrix(X)
sparse.save_npz('X50.npz', X)  # 保存
'''
X = sparse.load_npz('X50.npz')  # 读

# 取标签
lab = data.iloc[:, -1]
l = lab.values  # 使用tolist()也可以运行，结果一样！

x_train, x_test, y_train, y_test = train_test_split(X, l, test_size=0.5, random_state=15)

starttime = datetime.datetime.now()
#svclf = SVC(kernel = 'linear')
#svclf.fit(x_train,y_train)
#joblib.dump(svclf, 'svm50.pkl')
svclf = joblib.load('svm50.pkl')
preds = svclf.predict(x_test)
endtime = datetime.datetime.now()
print("SVM运行时间总计：" + str((endtime - starttime).seconds) + "秒\n")

themes = ["房产", "国际", "港澳", "能源", "汽车", "社会", "台湾", "体育", "文化", "娱乐"]
print("分类报告：")
print(classification_report(y_test, preds,target_names=themes))
print('整体准确率：'+str(accuracy_score(y_test, preds)))
print("混淆矩阵：")
print(themes)
print(confusion_matrix(y_test, preds))
