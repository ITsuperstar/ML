# encoding=utf-8
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
# 数据分析，朴素贝叶斯
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from scipy import sparse

# 读取数据
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("train-test.csv", encoding='utf-8')
# 取内容
con = data.iloc[:, 0]
corpus = con.values.tolist()  # 不使用tolist()也可以运行，结果一样！
#print(type(con.values))  #type(con.values)的结果是：numpy.ndarray
# 取标签
lab = data.iloc[:, 1]
l = lab.values  # 使用tolist()也可以运行，结果一样！
size = len(l)

vectorizer = CountVectorizer()  # 将文本中的词语转换为词频矩阵
X = vectorizer.fit_transform(corpus)  # 计算个词语出现的次数
word = vectorizer.get_feature_names()  # 获取词袋中所有文本关键词
#print(type(word))
print('\n' + str(len(word)))
#print(type(X)) #输出结果：<class 'scipy.sparse.csr.csr_matrix'>


'''
#X.toarray()会报错！
X = X.toarray()
trainnum = int(0.5 * size)
x_train = X[:trainnum]
x_test = X[trainnum:]
y_train = l[:trainnum]
y_test = l[trainnum:]
'''

x_train, x_test, y_train, y_test = train_test_split(X, l, test_size=0.5, random_state=15)
print(type(x_train))

# 调用MultinomialNB分类器
clf = MultinomialNB(alpha=0.000001).fit(x_train, y_train)
pre = clf.predict(x_test)
print(u"\n数据分析:")
# print(u"预测结果:", pre)
# print(u"真实结果:", y_test)
print(classification_report(y_test, pre))
'''
# K近邻算法
knn_model = KNeighborsClassifier(n_neighbors=10)
knn_model.fit(x_train, y_train)
pre = knn_model.predict(x_test)
print(classification_report(y_test, pre))
'''