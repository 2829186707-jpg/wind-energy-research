# -*- coding: utf-8 -*-
p = r'D:\桌面\风电\风电\report\_gen_report.py'
s = open(p, encoding='utf-8').read()
old = '''<div class="conclusion">
<h4>核心判断</h4>
<ul>
<li>整机板块选股逻辑：盈利修复弹性+结构升级。</li>
<li>金风科技：盈利确定性最强（动态PE **20.8倍**、扣非**+47.8%**），可作核心持仓。</li>
<li>三一重能：毛利率修复与份额提升兼具。</li>
<li>明阳智能/电气风电：海风放量与盈利拐点的弹性标的，待海风装机兑现后介入。</li>
</ul>
</div>
'''
assert old in s, 'not found'
s = s.replace(old, '')
open(p, 'w', encoding='utf-8').write(s)
print('OK')
