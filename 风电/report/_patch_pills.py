# -*- coding: utf-8 -*-
p = r'D:\桌面\风电\风电\report\_gen_report.py'
with open(p, 'r', encoding='utf-8') as f:
    s = f.read()

# 1) CSS
old_css = """.hp{fill:rgba(59,130,246,0.10);stroke:rgba(96,165,250,0.6);stroke-width:2;cursor:pointer;transition:fill .15s}
.hp:hover{fill:rgba(59,130,246,0.32)}
.hp .lbl{fill:#fff;stroke:#0f1117;stroke-width:4;paint-order:stroke;font-size:20px;font-weight:600;pointer-events:none}"""
new_css = """.hp{cursor:pointer}
.hp .pill{fill:#2563eb;fill-opacity:.88;stroke:none;transition:fill .15s,fill-opacity .15s}
.hp:hover .pill{fill:#1e40af;fill-opacity:1}
.hp .lbl{fill:#fff;font-size:15px;font-weight:600;pointer-events:none;text-anchor:middle}"""
assert old_css in s, 'CSS not found'
s = s.replace(old_css, new_css)

# 2) 陆上 SVG
old_land = """<svg viewBox="0 0 1000 1250" class="ov">
<g class="hp" onclick="openPart('blade')"><title>叶片</title><polygon points="320,480 740,480 530,60"/><text class="lbl" x="700" y="190" text-anchor="middle">叶片</text></g>
<g class="hp" onclick="openPart('gearbox')"><title>齿轮箱</title><rect x="466" y="430" width="44" height="34"/></g>
<g class="hp" onclick="openPart('bearing')"><title>轴承</title><rect x="514" y="430" width="30" height="34"/></g>
<g class="hp" onclick="openPart('generator')"><title>发电机</title><rect x="548" y="430" width="40" height="34"/></g>
<g class="hp" onclick="openPart('converter')"><title>变流器</title><rect x="466" y="468" width="60" height="30"/></g>
<g class="hp" onclick="openPart('nacelle')"><title>机舱总成</title><rect x="458" y="424" width="142" height="80" fill="none" stroke="#60a5fa" stroke-width="3" stroke-dasharray="8 6"/><text class="lbl" x="672" y="470" text-anchor="middle" font-size="17">机舱</text></g>
<g class="hp" onclick="openPart('install')"><title>塔筒/法兰</title><polygon points="490,958 572,958 546,512 516,512"/><text class="lbl" x="700" y="760" text-anchor="middle">塔筒/法兰</text></g>
<g class="hp" onclick="openPart('foundation')"><title>陆上基础</title><rect x="414" y="962" width="234" height="112"/><text class="lbl" x="300" y="1018" text-anchor="middle">基础</text></g>
</svg>"""

def pill(cx, cy, text, w):
    return (f'<g class="hp" onclick="openPart(\'{key_map[text]}\')"><title>{text}</title>'
            f'<rect class="pill" x="{cx-w//2}" y="{cy-12}" width="{w}" height="24" rx="12"/>'
            f'<text class="lbl" x="{cx}" y="{cy+5}">{text}</text></g>')

key_map = {'叶片':'blade','齿轮箱':'gearbox','轴承':'bearing','发电机':'generator','变流器':'converter',
           '机舱':'nacelle','塔筒/法兰':'install','基础':'foundation','塔筒':'install',
           '单桩/导管架':'monopile','海缆':'cable','海上升压站':'substation','施工安装':'installation'}

land_lines = [
    pill(700,178,'叶片',70),
    pill(440,530,'齿轮箱',84),
    pill(505,530,'轴承',70),
    pill(575,530,'发电机',84),
    pill(650,530,'变流器',84),
    pill(672,458,'机舱',70),
    pill(700,748,'塔筒/法兰',118),
    pill(300,1006,'基础',70),
]
new_land = '<svg viewBox="0 0 1000 1250" class="ov">\n' + '\n'.join(land_lines) + '\n</svg>'
assert old_land in s, 'land svg not found'
s = s.replace(old_land, new_land)

# 3) 海上 SVG
old_sea = """<svg viewBox="0 0 1000 1250" class="ov">
<g class="hp" onclick="openPart('blade')"><title>叶片</title><polygon points="170,480 590,480 360,60"/><text class="lbl" x="540" y="190" text-anchor="middle">叶片</text></g>
<g class="hp" onclick="openPart('gearbox')"><title>齿轮箱</title><rect x="314" y="430" width="42" height="34"/></g>
<g class="hp" onclick="openPart('bearing')"><title>轴承</title><rect x="360" y="430" width="28" height="34"/></g>
<g class="hp" onclick="openPart('generator')"><title>发电机</title><rect x="392" y="430" width="38" height="34"/></g>
<g class="hp" onclick="openPart('converter')"><title>变流器</title><rect x="314" y="468" width="56" height="30"/></g>
<g class="hp" onclick="openPart('nacelle')"><title>机舱总成</title><rect x="306" y="424" width="134" height="80" fill="none" stroke="#60a5fa" stroke-width="3" stroke-dasharray="8 6"/><text class="lbl" x="500" y="470" text-anchor="middle" font-size="17">机舱</text></g>
<g class="hp" onclick="openPart('install')"><title>塔筒/法兰</title><polygon points="320,960 400,960 384,510 336,510"/><text class="lbl" x="150" y="700" text-anchor="middle">塔筒</text></g>
<g class="hp" onclick="openPart('monopile')"><title>单桩/导管架</title><rect x="324" y="962" width="88" height="190"/><text class="lbl" x="555" y="1100" text-anchor="middle">单桩/导管架</text></g>
<g class="hp" onclick="openPart('cable')"><title>海缆</title><path d="M370,1120 C520,1090 620,1140 830,1120" fill="none" stroke-width="8"/><text class="lbl" x="650" y="1210" text-anchor="middle">海缆</text></g>
<g class="hp" onclick="openPart('substation')"><title>海上升压站</title><rect x="735" y="430" width="200" height="170"/><text class="lbl" x="835" y="408" text-anchor="middle" font-size="18">海上升压站</text></g>
<g class="hp" onclick="openPart('installation')"><title>施工安装</title><rect x="96" y="700" width="172" height="112" rx="14"/><text class="lbl" x="182" y="762" text-anchor="middle" font-size="18">施工安装</text></g>
</svg>"""
sea_lines = [
    pill(540,178,'叶片',70),
    pill(340,530,'齿轮箱',84),
    pill(405,530,'轴承',70),
    pill(475,530,'发电机',84),
    pill(550,530,'变流器',84),
    pill(500,458,'机舱',70),
    pill(150,688,'塔筒',70),
    pill(555,1088,'单桩/导管架',132),
    pill(650,1198,'海缆',70),
    pill(835,396,'海上升压站',118),
    pill(182,750,'施工安装',102),
]
new_sea = '<svg viewBox="0 0 1000 1250" class="ov">\n' + '\n'.join(sea_lines) + '\n</svg>'
assert old_sea in s, 'sea svg not found'
s = s.replace(old_sea, new_sea)

with open(p, 'w', encoding='utf-8') as f:
    f.write(s)
print('PATCH OK')
