# -*- coding: utf-8 -*-

import os
import re

themes = ["房产", "国际", "港澳", "能源", "汽车", "社会", "台湾", "体育", "文化", "娱乐"]
# num=[114195,111363,113930,95926,90569,117039,90372,122475,104825,111962]
# num=[114195,111363-10000,113930-10000,95926,90569,117039,90372,122475-20000,104825,111962]
themessub = ["国际1f-30", "国内1f-30", "体育1f-30"]
themessubnum = [101363, 103930,102475]
for i in range(len(themessub)):
    th = themessub[i]
    num = themessubnum[i]
    filename = th + '.txt'
    savefilename = th + 'f.txt'
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        with open(savefilename, 'a+', newline='', encoding='utf-8') as fsave:
            lines = f.readlines()
            count = 0
            for line in lines:
                if count >= num:
                    break
                fsave.write(line)
                count += 1
