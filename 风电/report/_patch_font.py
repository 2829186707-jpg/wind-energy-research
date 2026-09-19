# -*- coding: utf-8 -*-
import re
p = r'D:\桌面\风电\风电\report\_gen_report.py'
with open(p, 'r', encoding='utf-8') as f:
    s = f.read()

# 1) CSS: 字号 15 -> 18
s = s.replace('.hp .lbl{fill:#fff;font-size:15px;', '.hp .lbl{fill:#fff;font-size:18px;')

# 2) 胶囊宽度与高度统一放大（2字96 / 3字114 / 4字132 / 5字150 / 6字168，h=28）
#    按 title 字数重算
def fix_pill(m):
    inner = m.group(0)
    t = re.search(r'<title>([^<]+)</title>', inner).group(1)
    cx = int(re.search(r'<rect class="pill" x="(-?\d+)"', inner).group(1))
    cy = int(re.search(r'y="(-?\d+)"', inner).group(1))
    tx = int(re.search(r'<text class="lbl" x="(-?\d+)"', inner).group(1))
    n = len(t)
    w = {2:96, 3:114, 4:132, 5:150, 6:168}[n]
    # 重新居中
    new_x = tx - w//2
    new_y = cy  # cy 是旧 rect 的 y
    new_rect = f'<rect class="pill" x="{new_x}" y="{new_y}" width="{w}" height="28" rx="14"/>'
    new_text_y = new_y + 19  # 18px 字垂直居中
    inner = re.sub(r'<rect class="pill"[^/]*/>', new_rect, inner)
    inner = re.sub(r'(<text class="lbl" x="-?\d+" y=")-?\d+(")', lambda mm: mm.group(1)+str(new_text_y)+mm.group(2), inner)
    return inner

# 只处理 SVG 内的 g.hp
s = re.sub(r'<g class="hp" onclick="openPart\([^)]+\)">.*?</g>', fix_pill, s)

# 3) 海上升压站：下移贴平台顶部（平台顶部约 y=430）
#    当前 substation 的 rect 已被 fix_pill 重算，现在强制覆盖
old_sub = re.search(r'<g class="hp" onclick="openPart\(\'substation\'\)">.*?</g>', s).group(0)
new_sub = ('<g class="hp" onclick="openPart(\'substation\')"><title>海上升压站</title>'
           '<rect class="pill" x="760" y="430" width="150" height="28" rx="14"/>'
           '<text class="lbl" x="835" y="449">海上升压站</text></g>')
s = s.replace(old_sub, new_sub)

with open(p, 'w', encoding='utf-8') as f:
    f.write(s)
print('DONE')
