# encoding=utf-8
import csv

rows = [['姓名','年龄'],['张三',14],['李四',24],['王五',34]]
# with open('')
# csv 在写入的时候 默认每次写入会有一个空行作为分割
# 使用 newline='' 可以将空行去掉
with open('test1.csv','w',newline='',encoding='utf-8') as csv_file:
    # 获取一个csv对象进行写入
    writer = csv.writer(csv_file)
    for row in rows:
        # writerow 写入一行数据
        writer.writerow(row)

with open('test1.csv','r',encoding='utf-8') as read_file:
    # 获取一个csv对象进行读取
    reader = csv.reader(read_file)
    print([row for row in reader])

with open('test1.csv','r',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = [row for row in reader]
    print(rows)