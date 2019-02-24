#coding=utf-8
import jieba,math
import jieba.analyse
import os
import re

#jieba.cut主要有三种模式
#随便对一个动物园的评论进行分析
str_text="真是好久好久没来哈皮娜拉野生动物园了，记忆里还是小时候三四年级学校组织春游去的银河系"
#全模式cut_all=True
str_quan1=jieba.cut(str_text,cut_all=True)
print('全模式分词：{ %d}' % len(list(str_quan1)))
str_quan2=jieba.cut(str_text,cut_all=True)
print("/".join(str_quan2))
# print(str(str_1))   #为一个generator 用for循环可以得到分词的结果
# str_1_len=len(list(str_1))  #为什么？这里执行后后面.join 就不执行，求告知

#精准模式cut_all=False，默认即是
str_jing1=jieba.cut(str_text,cut_all=False)
print('精准模式分词：{ %d}' % len(list(str_jing1)))
str_jing2=jieba.cut(str_text,cut_all=False)
print("/".join(str_jing2))

#搜索引擎模式  cut_for_search
str_soso1=jieba.cut_for_search(str_text)
print('搜索引擎分词：{ %d}' % len(list(str_soso1)))
str_soso2=jieba.cut_for_search(str_text)
print("/".join(str_soso2))


# 引入TF-IDF关键词抽取接口
tfidf = jieba.analyse.extract_tags
# 引入TextRank关键词抽取接口
textrank = jieba.analyse.textrank

stopwords = []
for word in open("stop_words_me.txt", "r", encoding='utf-8'):
    stopwords.append(word.strip())
themes = ["财经", "国际", "国内", "能源", "汽车", "社会", "台湾", "体育", "文化", "娱乐"]
themes1=["1t"]

for th in themes1:
    filename=th+'.txt'
    savefilename=th+'f.txt'
    with open(savefilename, 'a+', newline='', encoding='utf-8') as fsave:
        with open(filename, 'r', newline='', encoding='utf-8') as fread:
            lines=fread.readlines()

            for line in lines:
                con = line.split(' ')
                stayed_line = ""
                stayed_line1 = ""
                for word in con:
                    if word not in stopwords:
                        stayed_line += word + " "
                        stayed_line1 += word
                print(stayed_line)
                print(stayed_line1)

                words = jieba.cut(stayed_line1, cut_all=False)
                print(' '.join(words))

                # 基于TF-IDF算法进行关键词抽取
                keywords = tfidf(stayed_line1, topK=10)
                print("keywords by tfidf:")
                rekeywords=" ".join(keywords)
                print(rekeywords)

                print("keywords by textrank:")
                # 基于TextRank算法进行关键词抽取
                keywords1 = textrank(stayed_line1,topK=10)
                # 输出抽取出的关键词
                print(" ".join(keywords1))

                fsave.write(rekeywords)
                fsave.write('\n')
                fsave.write(" ".join(keywords1))
                fsave.write('\n')
    print(th + "分词成功！")

'''
'''
