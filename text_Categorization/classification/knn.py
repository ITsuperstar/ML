# encoding=utf-8
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
from scipy import sparse
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


data = pd.read_csv("train-test1.csv", encoding='utf-8')
l = (data.iloc[:, 1]).values
X = sparse.load_npz('X.npz')

x_train, x_test, y_train, y_test = train_test_split(X, l, test_size=0.5, random_state=15)


knn_model = KNeighborsClassifier(n_neighbors=10)
knn_model.fit(x_train, y_train)
joblib.dump(knn_model, 'knn.pkl')
knn_model = joblib.load('knn.pkl')
preds = knn_model.predict(x_test)

themes = ["房产", "国际", "港澳", "能源", "汽车", "社会", "台湾", "体育", "文化", "娱乐"]
print("分类报告：")
print(classification_report(y_test, preds,target_names=themes))
print('整体准确率：'+str(accuracy_score(y_test, preds)))
print("混淆矩阵：")
print(themes)
print(confusion_matrix(y_test, preds))





