# -*- coding: utf-8 -*-
p = r'D:\桌面\风电\风电\report\_gen_report.py'
s = open(p, encoding='utf-8').read()

# 1. 删除整个 toolbar（回到顶部按钮）
old_tb = '''<div class="toolbar">
<button onclick="scrollTop0()">回到顶部</button>
</div>
'''
assert old_tb in s, 'toolbar not found'
s = s.replace(old_tb, '')

# 2. 三个标题改平实
R = [
('<h3>6.2 整机盈利拐点：三重信号确认</h3>',
 '<h3>6.2 整机盈利拐点：价格企稳与结构升级</h3>'),
('<h3>7.3 运营商：类公用事业+碳资产期权</h3>',
 '<h3>7.3 运营商：估值逻辑与选股</h3>'),
('<h3>8.1 三大核心预期差</h3>',
 '<h3>8.1 核心预期差</h3>'),
]
for o,n in R:
    assert o in s, o
    s = s.replace(o,n)

open(p,'w',encoding='utf-8').write(s)
print('OK')
