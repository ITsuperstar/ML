# -*- coding: UTF-8 -*-
import os
import csv
import pickle
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn import svm
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import datetime

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 2000)

class SVMClassify(object):
    def __init__(self):
        self.clf = svm.LinearSVC()
        self.test_flag=True
    def loadData(self, dir_path):
        y = []
        docs = []
        data = pd.read_csv(dir_path, encoding='utf-8')
        docs = data.iloc[:, 0].values.tolist()
        y = data.iloc[:, -1].values.tolist()
        return (y, docs)

    def getTfIdf(self, type,  docs):
        if type == 'train':
            vectorizer = TfidfVectorizer(max_df=0.5)
            tdm = vectorizer.fit_transform(docs)

            # 为了保证词典一致
            self.vocabulary = vectorizer.vocabulary_
            with open('./svm_out/vocabulary.txt', 'wb') as file:
                pickle.dump(self.vocabulary , file)
            with open('./svm_out/bag.txt', 'w') as file:
                for i in self.vocabulary:
                    file.write(str(i)+" "+str(self.vocabulary[i])+"\n")

            return tdm

        else:
            with open('./svm_out/vocabulary.txt', 'rb') as file2:
                self.vocabulary = pickle.load(file2)
            vectorizer = TfidfVectorizer(max_df=0.5, vocabulary = self.vocabulary)
            tdm = vectorizer.fit_transform(docs)
            return tdm

    def train(self, train_path):
        self.test_flag=False
        y, docs = self.loadData(train_path)

        # tf-idf计算
        print('开始计算tf-idf')
        tdm = self.getTfIdf('train', docs)

        # print(self.vocabulary)

        print('开始训练')
        self.clf.fit(tdm, y)
        self.model_presistence()
        # print(tdm)

    def test(self, test_path):
        if self.test_flag:
            self.train('./data/train/')
        y, docs = self.loadData(test_path)

         # tf-idf计算
        print('开始计算tf-idf')
        tdm = self.getTfIdf('test', docs)

        # 开始测试
        res = self.clf.predict(tdm)
        report = classification_report(y, res)
        confu = confusion_matrix(y, res)
        print(report)
        print(confu)
        with open("./svm_out/svm_result.txt","w")as f:
            f.write(str(report)+str(confusion_matrix))

    def model_presistence(self):
        fileObject = open('./svm_out/model/SVM.pkl', 'wb')
        pickle.dump(self.clf, fileObject)                                 #将SVC持久化
        fileObject.close()

    def calAccuracy(self):
        print(self.count)

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    svmIns = SVMClassify()
    svmIns.train('train1.csv')
    svmIns.test('test1.csv')
    endtime = datetime.datetime.now()
    print("SVM运行时间总计：" + str((endtime - starttime).seconds) + "秒\n")