# -*- coding: utf-8 -*-

import os
import re

themes = ["房产", "国际", "港澳", "能源", "汽车", "社会", "台湾", "体育", "文化", "娱乐"]
# num=[114195,111363,113930,65926+30000,90569,117039,90372,122475,69825+35000,111962]
# num=[114195,111363,113930,95926,90569,117039,90372,122475,104825,111962]

themesadd = ["能源1f-30", "文化1f-30"]
themesaddnum = [30000, 35000]
for i in range(len(themesadd)):
    th = themesadd[i]
    num = themesaddnum[i]
    filename = th + '.txt'
    savefilename = th + 'f.txt'
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        with open(savefilename, 'a+', newline='', encoding='utf-8') as fsave:
            lines = f.readlines()
            count = 0
            for line in lines:
                if count >= num:
                    break
                print(line)
                fsave.write(line)
                count += 1
