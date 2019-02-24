# encoding=utf-8
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
#数据分析，朴素贝叶斯
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
#读取数据
data = pd.read_csv("test1.csv", encoding='utf-8')
#取内容
con = data.iloc[:, 0]
arrs = con.values.tolist()
print(arrs)
corpus=arrs
#取标签
lab = data.iloc[:, 1]
l = lab.values.tolist()
size=len(l)
print(size)
print(l)


vectorizer = CountVectorizer()  # 将文本中的词语转换为词频矩阵
X = vectorizer.fit_transform(corpus)  # 计算个词语出现的次数
word = vectorizer.get_feature_names()  # 获取词袋中所有文本关键词
print(word)
print(X.toarray())

# 使用前8行数据集进行训练，最后两行数据集用于预测
print(u"\n数据分析:")
X = X.toarray()
x_train = X[:428]
x_test = X[428:]
# 1表示好评 0表示差评
y_train = l[:428]
y_test = l[428:]

# 调用MultinomialNB分类器
clf = MultinomialNB().fit(x_train, y_train)
pre = clf.predict(x_test)
print(u"预测结果:", pre)
print(u"真实结果:", y_test)

from sklearn.metrics import classification_report
print(classification_report(y_test, pre))