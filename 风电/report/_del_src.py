# -*- coding: utf-8 -*-
p = r'D:\桌面\风电\风电\report\_gen_report.py'
s = open(p, encoding='utf-8').read()
old = '<p>主要数据来源：彭博新能源财经、GWEC、水电水利规划设计总院、中国可再生能源学会风能专业委员会、平安证券、华泰证券及上市公司2026年半年报公告。</p>\n'
assert old in s, 'not found'
s = s.replace(old, '')
open(p, 'w', encoding='utf-8').write(s)
print('OK')
