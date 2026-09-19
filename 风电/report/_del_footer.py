# -*- coding: utf-8 -*-
p = r'D:\桌面\风电\风电\report\_gen_report.py'
s = open(p, encoding='utf-8').read()
old = '<div class="footer">风电行业深度研究 · 数据截至2026年9月 · 主要来源：GWEC/彭博新能源财经/水电水利规划设计总院/风能专委会/上市公司2026年半年报</div>'
assert old in s, 'not found'
s = s.replace(old, '')
open(p, 'w', encoding='utf-8').write(s)
print('OK')
