# -*- coding: utf-8 -*-
p = r'D:\桌面\风电\风电\report\_gen_report.py'
with open(p, 'r', encoding='utf-8') as f:
    s = f.read()
old = '<p>经济性改善的微观证据是运营商与产业资本的真实决策。2026年中海油在汕尾深远海设立两家新能源公司，注册资本**10亿元**，与明阳智能合资获取**500MW**海风项目并启动**2台18MW**大机组招标——从“基本不参与”到“10亿元主投”的转变，被市场解读为海上风电经济性发生根本改善的信号。</p>\n'
assert old in s, 'not found'
s = s.replace(old, '')
with open(p, 'w', encoding='utf-8') as f:
    f.write(s)
print('OK')
