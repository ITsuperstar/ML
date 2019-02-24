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

'''
# 读取数据
data = pd.read_csv("train-test1.csv", encoding='utf-8')

# 取内容
con = data.iloc[:, 0]
all_text = con.values.tolist()  # 不使用tolist()也可以运行，结果一样！
#print(type(con.values))  #type(con.values)的结果是：numpy.ndarray
# 取标签
lab = data.iloc[:, 1]
l = lab.values  # 使用tolist()也可以运行，结果一样！

data_train = pd.read_csv("train1.csv", encoding='utf-8')
train_texts = (data_train.iloc[:, 0]).values.tolist()
y_train = data_train.iloc[:, 1].values

data_test = pd.read_csv("test1.csv", encoding='utf-8')
test_texts = (data_test.iloc[:, 0]).values.tolist()
y_test = data_test.iloc[:, 1].values


#保存和读取稀疏矩阵
#sparse.save_npz('filename.npz', csr_matrix_variable)  # 保存
#csr_matrix_variable = sparse.load_npz('path.npz')  # 读

count_v0 = CountVectorizer()
counts_all = count_v0.fit_transform(all_text)
count_v1 = CountVectorizer(vocabulary=count_v0.vocabulary_)
counts_train = count_v1.fit_transform(train_texts)
print("the shape of train is " + repr(counts_train.shape))
count_v2 = CountVectorizer(vocabulary=count_v0.vocabulary_)
counts_test = count_v2.fit_transform(test_texts)
print("the shape of test is " + repr(counts_test.shape))

tfidftransformer = TfidfTransformer()
x_train = tfidftransformer.fit(counts_train).transform(counts_train)
x_test = tfidftransformer.fit(counts_test).transform(counts_test)
#print(type(x_train))
'''

'''
data = pd.read_csv("train-test1.csv", encoding='utf-8')
# 取内容
con = data.iloc[:, 0]
corpus = con.values.tolist()  # 不使用tolist()也可以运行，结果一样！
# 取标签
lab = data.iloc[:, 1]
l = lab.values  # 使用tolist()也可以运行，结果一样！

vectorizer = CountVectorizer()  # 将文本中的词语转换为词频矩阵
X = vectorizer.fit_transform(corpus)  # 计算个词语出现的次数
word = vectorizer.get_feature_names()  # 获取词袋中所有文本关键词
#保存和读取稀疏矩阵
sparse.save_npz('X.npz', X)  # 保存
X = sparse.load_npz('X.npz')  # 读
sparse.save_npz('Y.npz', l)  # 保存
l = sparse.load_npz('Y.npz')  # 读
'''

data = pd.read_csv("train-test1.csv", encoding='utf-8')
l = (data.iloc[:, 1]).values
X = sparse.load_npz('X.npz')

x_train, x_test, y_train, y_test = train_test_split(X, l, test_size=0.5, random_state=15)

clf = MultinomialNB(alpha = 0.01)
clf.fit(x_train, y_train)
joblib.dump(clf, 'nb.pkl')
clf = joblib.load('nb.pkl')
preds = clf.predict(x_test)

themes = ["房产", "国际", "港澳", "能源", "汽车", "社会", "台湾", "体育", "文化", "娱乐"]
print("分类报告：")
print(classification_report(y_test, preds,target_names=themes))
print('整体准确率：'+str(accuracy_score(y_test, preds)))
print("混淆矩阵：")
print(themes)
print(confusion_matrix(y_test, preds))




'''
svclf = SVC(kernel = 'linear')
svclf.fit(x_train,y_train)
joblib.dump(svclf, 'svm.pkl')
svclf = joblib.load('svm.pkl')
preds = svclf.predict(x_test)

themes = ["房产", "国际", "港澳", "能源", "汽车", "社会", "台湾", "体育", "文化", "娱乐"]
print("分类报告：")
print(classification_report(y_test, preds,target_names=themes))
print('整体准确率：'+str(accuracy_score(y_test, preds)))
print("混淆矩阵：")
print(themes)
print(confusion_matrix(y_test, preds))
'''