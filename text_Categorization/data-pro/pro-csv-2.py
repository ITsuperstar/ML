# -*- coding: utf-8 -*-

import os
import csv

d = {"房产": 0, "国际": 1, "港澳": 2, "能源": 3, "汽车": 4, "社会": 5, "台湾": 6, "体育": 7, "文化": 8, "娱乐": 9}
themes = ["房产", "国际", "港澳", "能源", "汽车", "社会", "台湾", "体育", "文化", "娱乐"]
# num=[111568,111363-10000,98900,65926+30000,90569,117039,90372,122475-20000,69825+35000,111962]
num = [111568, 101363, 98900, 95926, 90569, 117039, 90372, 102475, 104825, 111962]
totalnum=1024999

'''
#分配每个类别的训练集的数量
train_rate=[0.5622, 0.5067, 0.5189, 0.500, 0.500, 0.5728, 0.50, 0.5121, 0.523, 0.5534]
for i in num:
    j=1-50000/i
    train_rate.append(round(j,4))
print(train_rate)
print("总的样本数："+sum(num))
'''
with open("test1.csv", 'r', newline='', encoding='utf-8') as ftest:
    with open("train-test1.csv", 'a+', newline='', encoding='utf-8') as f:
        lines=csv.reader(ftest)
        rows = [row for row in lines]
        w = csv.writer(f)
        w.writerows(rows[1:])
