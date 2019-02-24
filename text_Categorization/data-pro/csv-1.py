# -*- coding: utf-8 -*-

import csv
import os

d = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
c=[0]*10
with open("train-test.csv", 'r', newline='', encoding='utf-8') as ftest:
    with open("result.txt", 'a+', newline='', encoding='utf-8') as f:
        lines = csv.reader(ftest)
        rows = [row for row in lines][1:]
        for r in rows:
            index=int(r[1])
            label=d[index]+str(c[index])
            c[index] += 1
            f.write(label)
            f.write(' ')
            f.write(r[0])
            f.write('\n')
