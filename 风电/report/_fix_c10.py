# -*- coding: utf-8 -*-
p = r'D:\桌面\风电\风电\report\_gen_report.py'
with open(p, 'r', encoding='utf-8') as f:
    s = f.read()

old = """c9.on('click',function(p){var v=window['D_LAYER'][p.data.name];if(v)openModal(v[0],v[1],v[2]);});
window.addEventListener('resize',function(){
var c10=echarts.init(gd('chart-sens'));"""
new = """c9.on('click',function(p){var v=window['D_LAYER'][p.data.name];if(v)openModal(v[0],v[1],v[2]);});
var c10=echarts.init(gd('chart-sens'));"""
assert old in s, 'part1 not found'
s = s.replace(old, new)

# 末尾去掉多余闭合
old2 = "window.addEventListener('resize',function(){[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10].forEach(function(c){c.resize();});});});"
new2 = "window.addEventListener('resize',function(){[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10].forEach(function(c){c.resize();});});"
assert old2 in s, 'part2 not found'
s = s.replace(old2, new2)

with open(p, 'w', encoding='utf-8') as f:
    f.write(s)
print('FIXED')
