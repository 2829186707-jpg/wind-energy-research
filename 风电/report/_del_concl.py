# -*- coding: utf-8 -*-
p = r'D:\桌面\风电\风电\report\_gen_report.py'
s = open(p, encoding='utf-8').read()
old = '''<div class="conclusion">
<h4>核心判断</h4>
<ul>
<li>风电的收入来源已从财政补贴切换为市场电价、机制保护与环境溢价的组合。</li>
<li>谁能以最低成本获取资源、以最高效率运营项目，谁就能在全面入市时代赚到超额收益。</li>
<li>设备环节的降本能力（大型化、国产化）与运营环节的精细化能力，是贯穿整个“十五五”的两条主线。</li>
</ul>
</div>
'''
assert old in s, 'not found'
s = s.replace(old, '')
open(p, 'w', encoding='utf-8').write(s)
print('OK')
