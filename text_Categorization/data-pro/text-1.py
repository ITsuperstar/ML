# encoding=utf-8
import os
import re

filename='1.txt'
with open(filename, 'a', newline='', encoding='utf-8') as f:
    f.write("中国国过过")
    f.write("\n")

str = u'''　　中新社布加勒斯特11月26日电  中国－中东欧国家领导人会晤26日在罗马尼亚布加勒斯特举行。与会各方围绕“合作共赢，共同发展”的主题，共同制定和发表《中国－中东欧国家合作布加勒斯特纲要》。　　在纲要中，与会各方一致认为中国－中东欧国家合作契合了中国和中东欧国家的各自发展特点与合作需求，符合中国和中东欧国家人民的共同愿望和利益。　　与会各方强调中国－中东欧国家合作与中欧全面战略伙伴关系相辅相成，并行不悖，愿继续本着相互尊重、平等互利、合作共赢的原则，加强和深化中国－中东欧国家合作，致力于将中国－中东欧国家合作打造成为中欧合作的增长点，服务各自发展，造福各国人民，促进世界和平与稳定，并为处于不同文明、不同制度和不同发展阶段的国家和谐相处、共同发展提供有益经验。　　这份纲要旨在推动中国－中东欧国家合作进一步发展，具体而言，它涵盖双方投资经贸、金融、互联互通、人文交流、地方等六大领域的合作内容，对双方合作具有指引性作用。　　纲要指出，每年举行中国－中东欧国家领导人会晤，梳理合作成果，规划合作方向。根据合作发展情况，适时考虑制定中期合作规划。　　关于促进双方投资经贸合作，纲要认为，要坚决反对任何形式的保护主义，致力于促进相互投资，提升经贸合作规模和水平。在扩大贸易规模的同时，努力减少现有贸易不平衡现象；宣布2014年为“中国－中东欧国家合作投资经贸促进年”，并在促进年框架内举办中国和中东欧国家经贸促进部长级会议等一系列活动。　　关于扩大金融合作，纲要提出四项具体合作措施，包括中国和中东欧国家加强协调，鼓励各自金融机构开展灵活多样的合作，充分发挥“100亿美元专项贷款”对中国－中东欧国家经贸合作的促进作用；支持中国和中东欧国家符合条件、有意愿的机构投资对方银行间债券市场等。　　纲要对推进双方互联互通合作也作出具体规划。纲要说，要积极探讨构建中国和中东欧国家之间的国际铁路运输大通道，推动企业在铁路沿线建设保税区和物资分拨中心，打造中欧物流新动脉；在互利互惠原则下，加强在公路、铁路、港口、机场等基础设施建设领域的合作等。　　另外，纲要还表示要采取有效措施便利人员往来。例如：中方欢迎罗马尼亚、捷克等中东欧国家为中国公民申办签证、居留实行便利措施，宣布将中东欧16国全部列入外国人72小时免签过境北京、上海等口岸名单。（完）
'''
p = re.compile(u'[\u4e00-\u9fa5]')
res = re.findall(p, str)
result = ''.join(res)
print(result)
print("over")

#一次读一行，直至读完
with open(filename, 'r', newline='', encoding='utf-8') as f:
    line=f.readline()
    while line:
        print(line)
        line = f.readline()
#一次读完，然后迭代
with open(filename, 'r', newline='', encoding='utf-8') as f:
    lines=f.readlines()
    s=''
    for line in lines:
        s += line
    print(s)
