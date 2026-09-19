# -*- coding: utf-8 -*-
p = r'D:\桌面\风电\风电\report\_gen_report.py'
with open(p, 'r', encoding='utf-8') as f:
    s = f.read()
old = '<button id="btn-red" onclick="toggleMode()">只看关键数据</button>\n'
assert old in s, 'btn not found'
s = s.replace(old, '')
with open(p, 'w', encoding='utf-8') as f:
    f.write(s)
print('OK')
