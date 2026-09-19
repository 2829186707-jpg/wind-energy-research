# -*- coding: utf-8 -*-
p = r'D:\桌面\风电\风电\report\_gen_report.py'
s = open(p, encoding='utf-8').read()
old = '''<div class="conclusion">
<h4>图解使用说明</h4>
<ul>
<li>点击<b>叶片/齿轮箱/轴承/发电机/变流器/机舱/海缆/升压站/施工安装</b>直接查看对应环节分析。</li>
<li>点击<b>塔筒/单桩</b>等装机环节，会先进入细分面板，可选择<b>塔筒、法兰、单桩、导管架、陆上基础</b>再查看详情。</li>
<li>机舱内细色块对应<b>齿轮箱/轴承/发电机/变流器</b>，机舱虚线框点击查看总成说明。</li>
</ul>
</div>
'''
assert old in s, 'not found'
s = s.replace(old, '')
open(p, 'w', encoding='utf-8').write(s)
print('OK')
