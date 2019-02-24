# encoding=utf-8
import jieba, math
import jieba.analyse
import os
import re

stopwords = []
for word in open("stop_words.txt", "r", encoding='utf-8'):
    stopwords.append(word.strip())
themes = ["财经", "国际", "国内", "能源", "汽车", "社会", "台湾", "体育", "文化", "娱乐"]
'''
#将整个txt文件一次进行分词，程序似乎跑不动！
for th in themes:
    filename=th+'.txt'
    savefilename=th+'1.txt'
    with open(savefilename, 'a+', newline='', encoding='utf-8') as fsave:
        with open(filename, 'r', newline='', encoding='utf-8') as fread:
            lines=fread.read()
            words = jieba.cut(lines, cut_all=False)
            stayed_line = ""
            for word in words:
                if word not in stopwords:
                    stayed_line += word + " "
            fsave.write(stayed_line)
            print(th+"分词成功！")
'''
for th in themes:
    filename = th + '.txt'
    savefilename = th + '1.txt'
    with open(savefilename, 'a+', newline='', encoding='utf-8') as fsave:
        with open(filename, 'r', newline='', encoding='utf-8') as fread:
            lines = fread.readlines()
            for line in lines:
                words = jieba.cut(line, cut_all=False)
                stayed_line = ""
                for word in words:
                    if word not in stopwords:
                        stayed_line += word + " "
                fsave.write(stayed_line)
    print(th + "分词成功！")
