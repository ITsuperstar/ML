# -*- coding: utf-8 -*-

import pymysql
import csv

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "news", charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
themes = ["地方", "国内", "法治", "房产", "体育", "国际", "社会", "财经", "文化", "台湾", "图片", "能源", "汽车", "娱乐", "港澳", "侨界", "教育",
          "金融", "军事", "证券", "报摘", "留学", "侨乡", "华人", "华教", "生活", "健康", "视频", "I  T"]
'''
#创建所有类型的csv文件
for th in themes:
    filename=th+'.csv'
    with open(filename,'w',newline='',encoding='utf-8') as csv_file:
        pass
'''
#这种写入数据的方式很慢，需要改进！改进思路：数据插入文件时，不要一条一条的插入，应该成批的插入，减少打开文件的次数！改进方法：在pro-text程序中！
try:
    for i in range(17):
        startid = 100000 * i
        endid = 100000 * (i + 1)  # maxid=1686675
        sql = "select content,theme from news where id>=" + str(startid) + " and id<" + str(endid)
        cursor.execute(sql)
        count = cursor.rowcount
        while count:
            count = count - 1
            row = cursor.fetchone()
            if row[1] in themes:
                try:
                    fname = row[1] + '.csv'
                    with open(fname, 'a+', newline='', encoding='utf-8') as csvfile:
                        temp=row[0]
                        temp = temp.replace(' ', '')
                        temp = temp.replace('\n', '')
                        writer = csv.writer(csvfile)
                        writer.writerow([temp, row[1]])
                except Exception as fe:
                    print(row[1] + "文件写入异常" + str(fe))
except Exception as e:
    print(str(e))  # 根据报错信息提示错误

# 关闭数据库连接
db.close()
