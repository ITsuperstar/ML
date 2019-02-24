# -*- coding: utf-8 -*-

import pymysql
import re

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "news", charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
themes = ["财经", "国际", "国内", "能源", "汽车", "社会", "台湾", "体育", "文化", "娱乐"]
#num=[114195,111363,113930,65926,90569,117039,90372,122475,69825,111962]

'''
#创建所有类型的txt文件
for th in themes:
    filename=th+'.txt'
    with open(filename,'w',newline='',encoding='utf-8') as f:
        pass
'''
for th in themes:
    try:
        txtnumber=0
        for i in range(17):
            if txtnumber>110000:
                break
            startid = 100000 * i
            endid = 100000 * (i + 1)  # maxid=1686675
            sql = "select content from news where id>=" + str(startid) + " and id<" + str(endid)+ " and theme='" + th +"'"
            cursor.execute(sql)
            count = cursor.rowcount
            fname = th + '.txt'
            with open(fname, 'a+', newline='', encoding='utf-8') as f:
                while count:
                    try:
                        count = count - 1
                        txtnumber += 1
                        row = cursor.fetchone()
                        p = re.compile(u'[\u4e00-\u9fa5]')
                        res = re.findall(p, row[0])
                        result = ''.join(res)
                        f.write(result)
                        f.write('\n')
                    except Exception as fe:
                        print(th + "文件写入异常" + str(fe))
        print(txtnumber)
    except Exception as e:
        print(str(e))  # 根据报错信息提示错误

# 关闭数据库连接
db.close()
