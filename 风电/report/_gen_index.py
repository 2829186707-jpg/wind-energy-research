# -*- coding: utf-8 -*-
"""从 _doc_structure.json 生成风电分析网页 index.html（含标红高亮、表格、图表）"""
import json, html, os, re

SRC = r'D:\桌面\风电\风电\report\_doc_structure.json'
OUT = r'D:\桌面\风电\风电\report\index.html'
BASE = os.path.dirname(SRC)

data = json.load(open(SRC, encoding='utf-8'))
paras = data['paras']
tables = data['tables']

FIG_MAP = {
    '图3-1': 'fig3-1_装机路径.png',
    '图3-2': 'fig3-2_全球海风预测.png',
    '图4-1': 'fig4-1_整机成本构成.png',
    '图4-2': 'fig4-2_轴承国产化.png',
    '图5-1': 'fig5-1_整机份额.png',
    '图5-2': 'fig5-2_2026H1中标.png',
    '图6-1': 'fig6-1_海风投资构成.png',
    '图6-2': 'fig6-2_海缆电压.png',
    '图6-3': 'fig6-3_海缆格局.png',
    '图7-1': 'fig7-1_陆海投资对比.png',
    '图7-2': 'fig7-2_海风IRR敏感性.png',
    '图8-1': 'fig8-1_整机业绩.png',
    '图8-2': 'fig8-2_估值对比.png',
    '图9-1': 'fig9-1_投资分层.png',
}

def esc(t): return html.escape(t, quote=False)

def render_para(p):
    text = p['text']
    reds = p.get('red') or []
    if not reds:
        return '<p>' + esc(text) + '</p>'
    body = esc(text)
    marks = []
    for r in reds:
        rr = esc(r)
        if rr in body:
            marks.append(rr)
    for rr in sorted(set(marks), key=len, reverse=True):
        body = body.replace(rr, '<mark>' + rr + '</mark>', 1)
    return '<p class="has-red">' + body + '</p>'

sections = []
table_idx = 0
body = []
sec_id = None
sec_title = ''
i = 0
n = len(paras)
while i < n:
    p = paras[i]
    lv = p.get('level')
    if lv == 1:
        if sec_id is not None and body:
            sections.append((sec_id, sec_title, body))
        sec_id = 'sec' + str(len(sections) + 1)
        sec_title = p['text']
        body = []
        i += 1
        continue
    elif lv == 2:
        body.append('<h3>' + esc(p['text']) + '</h3>')
        i += 1
        continue
    elif lv == 3:
        body.append('<h4 class="h4-sub">' + esc(p['text']) + '</h4>')
        i += 1
        continue
    else:
        t = p['text']
        fig_match = None
        for key in FIG_MAP:
            if t.startswith(key + ' '):
                fig_match = key
                break
        if fig_match:
            fname = FIG_MAP[fig_match]
            fpath = 'charts/' + fname
            if os.path.exists(os.path.join(BASE, 'charts', fname)):
                body.append('<figure class="fig"><img src="' + fpath + '" alt="' + esc(t) + '"><figcaption>' + esc(t) + '</figcaption></figure>')
            else:
                body.append('<p><strong>' + esc(t) + '</strong></p>')
            i += 1
            continue
        if re.match(r'^表\d+-\d+', t):
            if table_idx < len(tables):
                tbl = tables[table_idx]
                table_idx += 1
                rows_html = []
                for ri, row in enumerate(tbl):
                    if ri == 0:
                        rows_html.append('<tr>' + ''.join('<th>' + esc(c) + '</th>' for c in row) + '</tr>')
                    else:
                        rows_html.append('<tr>' + ''.join('<td>' + esc(c) + '</td>' for c in row) + '</tr>')
                body.append('<p class="tbl-title">' + esc(t) + '</p>')
                body.append('<div class="tbl-wrap"><table>' + ''.join(rows_html) + '</table></div>')
            else:
                body.append('<p><strong>' + esc(t) + '</strong></p>')
            i += 1
            continue
        body.append(render_para(p))
        i += 1

if body:
    sections.append((sec_id, sec_title, body))

nav_html = ''.join('<a href="#' + sid + '">' + esc(st) + '</a>' for sid, st, _ in sections)

sec_html_all = []
for sid, st, body_html in sections:
    inner = '\n'.join(body_html)
    sec_html_all.append('<div class="section" id="' + sid + '"><h2>' + esc(st) + '</h2>\n' + inner + '</div>')

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif;background:#0f1117;color:#e4e6eb;line-height:1.75}
.container{max-width:1280px;margin:0 auto;padding:20px}
.nav{position:sticky;top:0;background:rgba(15,17,23,0.96);backdrop-filter:blur(10px);padding:14px 0;border-bottom:1px solid #2a2d3a;z-index:100;display:flex;flex-wrap:wrap;gap:6px;justify-content:center}
.nav a{color:#8b8fa3;text-decoration:none;padding:6px 12px;border-radius:6px;font-size:13px;transition:all .2s}
.nav a:hover{color:#fff;background:#2563eb}
.section{margin:36px 0;padding:30px;background:#181b24;border-radius:12px;border:1px solid #252836}
h1{font-size:34px;margin-bottom:8px;background:linear-gradient(135deg,#60a5fa,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
h2{font-size:23px;margin-bottom:18px;color:#fff;border-left:4px solid #3b82f6;padding-left:12px}
h3{font-size:17px;margin:22px 0 12px;color:#93c5fd}
.h4-sub{font-size:15px;margin:18px 0 10px;color:#a5b4fc}
p{font-size:14px;color:#c9cdd8;margin:10px 0;text-align:justify}
mark{background:rgba(239,68,68,0.16);color:#fca5a5;padding:1px 4px;border-radius:3px;border-bottom:2px solid #ef4444;font-weight:600}
.has-red{border-left:3px solid rgba(239,68,68,0.5);padding-left:12px;background:linear-gradient(90deg,rgba(239,68,68,0.06),transparent)}
.fig{margin:18px 0;text-align:center}
.fig img{display:block;max-width:100%;margin:0 auto;border-radius:8px;border:1px solid #2a2d3a}
.fig figcaption{font-size:12px;color:#8b8fa3;margin-top:8px}
.tbl-title{font-size:13px;color:#60a5fa;font-weight:600;margin:16px 0 6px}
.tbl-wrap{overflow-x:auto;margin:10px 0}
table{width:100%;border-collapse:collapse;font-size:13px}
th{background:#252836;padding:9px 12px;text-align:left;color:#93c5fd;font-weight:600;border-bottom:2px solid #3b82f6;white-space:nowrap}
td{padding:9px 12px;border-bottom:1px solid #252836}
tr:hover{background:rgba(59,130,246,0.05)}
.toolbar{position:sticky;top:52px;z-index:90;display:flex;justify-content:center;gap:10px;padding:10px 0;background:rgba(15,17,23,0.9);backdrop-filter:blur(8px);border-bottom:1px solid #252836}
.toolbar button{background:#1e2230;border:1px solid #2a2d3a;color:#8b8fa3;padding:6px 18px;border-radius:6px;cursor:pointer;font-size:13px;transition:all .2s}
.toolbar button:hover,.toolbar button.active{background:#2563eb;color:#fff;border-color:#2563eb}
body.mode-red p:not(.has-red){display:none}
body.mode-red .fig,body.mode-red .tbl-wrap,body.mode-red .tbl-title{display:none}
body.mode-red h3,body.mode-red h4{display:none}
.footer{text-align:center;padding:36px 20px;color:#6b7280;font-size:12px;border-top:1px solid #252836;margin-top:50px}
@media(max-width:768px){.section{padding:20px 14px}.nav a{font-size:12px;padding:10px 10px;min-height:44px;display:inline-flex;align-items:center}h2{font-size:19px}h3{font-size:15px}p{font-size:14px}.toolbar button{min-height:44px}}
"""

page = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>风电行业深度学习 · 私募研究员二面备战手册（网页版）</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230F1117'/%3E%3Ccircle cx='32' cy='32' r='5' fill='%233B82F6'/%3E%3Cpath d='M32 32 L32 12 M32 32 L50 24 M32 32 L47 42 M32 32 L14 26 M32 32 L19 44' stroke='%2360A5FA' stroke-width='4' stroke-linecap='round'/%3E%3C/svg%3E">
<style>
""" + CSS + """</style>
</head>
<body>
<div class="nav">
""" + nav_html + """
</div>
<div class="container">
<div class="toolbar">
<button id="btn-red" onclick="toggleMode()">只看标红重点</button>
<button onclick="scrollTop0()">回到顶部</button>
</div>
""" + '\n'.join(sec_html_all) + """
<div class="footer">风电行业深度学习 · 私募研究员二面备战手册（网页版） · 数据截至2026年9月 · 标红内容为手册重点，可在面试演示中一键聚焦</div>
</div>
<script>
function toggleMode(){var b=document.getElementById('btn-red');document.body.classList.toggle('mode-red');b.classList.toggle('active');b.textContent=document.body.classList.contains('mode-red')?'显示全部内容':'只看标红重点';}
function scrollTop0(){window.scrollTo({top:0,behavior:'smooth'});}
</script>
</body>
</html>"""

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(page)
print('OK ->', OUT, os.path.getsize(OUT), 'bytes | sections:', len(sections), '| tables used:', table_idx)
