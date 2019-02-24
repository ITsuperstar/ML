# encoding=utf-8
import csv

import jieba, math
import jieba.analyse
import os
import re
import numpy as np
from scipy import sparse
from scipy.sparse.csr import csr_matrix

# 引入TF-IDF关键词抽取接口
tfidf = jieba.analyse.extract_tags
'''
themes = ["房产", "国际", "港澳", "能源", "汽车", "社会", "台湾", "体育", "文化", "娱乐"]
for th in themes:
    filename = th + '1f-30.txt'
    savefilename = 'fword-all.txt'
    with open(savefilename, 'a+', newline='', encoding='utf-8') as fsave:
        with open(filename, 'r', newline='', encoding='utf-8') as fread:
            lines = fread.read()
            con = lines.split()
            con = ''.join(con)
            # 基于TF-IDF算法进行关键词抽取
            keywords1 = tfidf(con, topK=1200, allowPOS=('n'))
            # 抽取出的关键词
            top = " ".join(keywords1)
            print(top)
            fsave.write(top)
            fsave.write('\n')
    print(th + "成功提取1200个关键词！")

'''
keyw = []  # 存放所有的词向量
with open('fword-all.txt', 'r', newline='', encoding='utf-8') as fread:
    lines = fread.readlines()
    for line in lines:
        key = line.split()
        keyw += key[:50]
    s = set(keyw)
    keyw = list(s)
    keyw.append('label')
    print(len(keyw))

savefilename = 'fword-all.csv'
with open(savefilename, 'a+', newline='', encoding='utf-8') as fsave:
    writer = csv.writer(fsave)
    writer.writerow(keyw)
    themes = ["房产", "国际", "港澳", "能源", "汽车", "社会", "台湾", "体育", "文化", "娱乐"]
    for i in range(len(themes)):
        filename = themes[i] + '1f-30.txt'
        with open(filename, 'r', newline='', encoding='utf-8') as fread:
            lines = fread.readlines()
            for line in lines:
                temp = line.split()
                w = [0] * len(keyw)
                for t in temp:
                    if t in keyw:
                        indx = keyw.index(t)
                        w[indx] = w[indx] + 1
                w[-1] = i
                writer.writerow(w)
        print(themes[i] + "统计成功!")
#sparse.save_npz('x1000.npz', csr_matrix(np.array(x1000)))  # 保存稀疏矩阵
#sparse.save_npz('y1000.npz', csr_matrix(np.array(y1000)))
