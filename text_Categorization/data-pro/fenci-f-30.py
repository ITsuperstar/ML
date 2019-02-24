# encoding=utf-8
import jieba, math
import jieba.analyse
import os
import re

# 引入TF-IDF关键词抽取接口
tfidf = jieba.analyse.extract_tags

stopwords = []
for word in open("stop_words_me.txt", "r", encoding='utf-8'):
    stopwords.append(word.strip())
themes = ["房产", "国际", "港澳", "能源", "汽车", "社会", "台湾", "体育", "文化", "娱乐"]
for th in themes:
    filename=th+'.txt'
    savefilename=th+'1f-30.txt'
    with open(savefilename, 'a+', newline='', encoding='utf-8') as fsave:
        with open(filename, 'r', newline='', encoding='utf-8') as fread:
            lines=fread.readlines()
            for line in lines:
                con = line.split(' ')
                if len(con)>=2:
                    con=con[1:]
                stayed_line1 = ""
                for word in con:
                    if word not in stopwords:
                        stayed_line1 += word

                # 基于TF-IDF算法进行关键词抽取
                keywords1 = tfidf(stayed_line1, topK=30, allowPOS=('n'))

                # 抽取出的关键词
                top30=" ".join(keywords1)
                fsave.write(top30)
                fsave.write('\n')
    print(th + "提取关键词成功！")

'''
'''
