# encoding=utf-8
import jieba, math
import jieba.analyse
import os
import re

# 引入TextRank关键词抽取接口
textrank = jieba.analyse.textrank

stopwords = []
for word in open("stop_words_me.txt", "r", encoding='utf-8'):
    stopwords.append(word.strip())
themes = ["财经", "国际", "国内", "能源", "汽车", "社会", "台湾", "体育", "文化", "娱乐"]

for th in themes:
    filename=th+'1.txt'
    savefilename=th+'1f.txt'
    with open(savefilename, 'a+', newline='', encoding='utf-8') as fsave:
        with open(filename, 'r', newline='', encoding='utf-8') as fread:
            lines=fread.readlines()
            for line in lines:
                con = line.split(' ')
                stayed_line1 = ""
                for word in con:
                    if word not in stopwords:
                        stayed_line1 += word

                # 基于TextRank算法进行关键词抽取
                keywords1 = textrank(stayed_line1,topK=10)
                # 抽取出的关键词
                top10=" ".join(keywords1)
                fsave.write(top10)
                fsave.write('\n')
    print(th + "提取关键词成功！")

'''
'''
