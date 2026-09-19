# -*- coding: utf-8 -*-
"""风电手册 第6-7章 图表生成"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 200

OUT = r'C:\Users\veken\Desktop\风电\report\charts'
os.makedirs(OUT, exist_ok=True)

# ============ 图6-1 海风单GW投资构成 ============
fig, ax = plt.subplots(figsize=(8.2, 4.8))
labels = ['整机（含塔筒）', '塔基与基础\n（单桩/导管架）', '海缆', '施工安装', '叶片', '其他']
vals = [38, 23, 12, 12, 8, 7]   # 海风产业链产值占比口径（整机35-40、基础20-25、海缆10-15、施工约10-15、叶片10-12、其他）
colors = ['#1A2E4B', '#2F4A3B', '#4E79A7', '#5A8FB8', '#7BA3C9', '#B0B8C4']
explode = [0.03, 0.05, 0.08, 0.03, 0, 0]
w, t, a = ax.pie(vals, labels=labels, autopct='%d%%', colors=colors, explode=explode,
                 startangle=90, counterclock=False, pctdistance=0.78,
                 textprops={'fontsize': 9})
for wgt in w: wgt.set_linewidth(0.8); wgt.set_edgecolor('white')
plt.title('图6-1 海上风电单GW投资构成（行业口径）', fontsize=11, pad=14)
plt.tight_layout(); plt.savefig(os.path.join(OUT, 'fig6-1_海风投资构成.png')); plt.close()

# ============ 图6-2 海缆电压等级升级路线 ============
fig, ax = plt.subplots(figsize=(8.2, 4.4))
stages = ['8-10MW\n阵列35kV', '12-15MW\n阵列66kV', '15-20MW\n送出330kV', '20MW+\n直流±525kV']
x = range(len(stages))
y = [35, 66, 330, 525]
bars = ax.bar(x, y, width=0.5, color=['#B0B8C4', '#7BA3C9', '#4E79A7', '#1A2E4B'])
for b, v in zip(bars, y):
    ax.text(b.get_x()+b.get_width()/2, v+15, f'{v}kV', ha='center', fontsize=9, fontweight='bold')
ax.set_xticks(list(x)); ax.set_xticklabels(stages, fontsize=9)
ax.set_ylabel('电压等级（kV）')
ax.set_ylim(0, 620)
ax.set_title('图6-2 海缆电压等级随机组大型化跃迁路线', fontsize=11)
ax.grid(axis='y', linestyle='--', alpha=0.4)
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(os.path.join(OUT, 'fig6-2_海缆电压.png')); plt.close()

# ============ 图6-3 海缆竞争格局 ============
fig, ax = plt.subplots(figsize=(8.2, 4.2))
comps = ['中天科技', '东方电缆', '亨通光电', '其他']
shares = [37, 25, 18, 20]   # 中天36-38%口径，东方约25%，亨通约18%，其余
colors = ['#1A2E4B', '#4E79A7', '#7BA3C9', '#B0B8C4']
bars = ax.bar(comps, shares, width=0.5, color=colors)
for b, v in zip(bars, shares):
    ax.text(b.get_x()+b.get_width()/2, v+0.8, f'{v}%', ha='center', fontsize=10, fontweight='bold')
ax.set_ylabel('国内海缆市场份额（%）')
ax.set_ylim(0, 45)
ax.set_title('图6-3 国内海缆市场竞争格局（估算口径）', fontsize=11)
ax.grid(axis='y', linestyle='--', alpha=0.4)
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(os.path.join(OUT, 'fig6-3_海缆格局.png')); plt.close()

# ============ 图7-1 陆风vs海风单GW投资对比 ============
fig, ax = plt.subplots(figsize=(8.2, 4.6))
cats = ['陆上风电', '近海风电', '深远海风电']
cost = [50, 120, 155]   # 陆上45-55取50；近海110-130取120；深远海130-180取155（亿元/GW）
colors = ['#B0B8C4', '#4E79A7', '#1A2E4B']
bars = ax.bar(cats, cost, width=0.45, color=colors)
for b, v in zip(bars, cost):
    ax.text(b.get_x()+b.get_width()/2, v+3, f'{v}亿元/GW', ha='center', fontsize=10, fontweight='bold')
ax.set_ylabel('单位投资（亿元/GW）')
ax.set_ylim(0, 185)
ax.set_title('图7-1 陆风与海风单GW单位投资对比（2026年口径）', fontsize=11)
ax.grid(axis='y', linestyle='--', alpha=0.4)
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(os.path.join(OUT, 'fig7-1_陆海投资对比.png')); plt.close()

# ============ 图7-2 海风IRR敏感性（电价×利用小时） ============
fig, ax = plt.subplots(figsize=(8.2, 4.6))
hours = np.array([3000, 3200, 3400, 3600, 3800])
prices = np.array([0.30, 0.35, 0.40, 0.45])  # 元/kWh
for p in prices:
    # 简化模型：IRR ≈ 电价×利用小时 - 单位运维 - 财务成本，用相对刻度示意
    irr = (p*hours/1000 - 0.55) * 22 + 2.0
    ax.plot(hours, irr, marker='o', linewidth=1.8, label=f'电价 {p:.2f}元/kWh')
ax.axhline(6.5, color='#E8720C', linestyle='--', linewidth=1.2, label='市场要求回报线（约6.5%）')
ax.set_xlabel('年等效利用小时（h）'); ax.set_ylabel('项目全投资IRR（%，示意模型）')
ax.set_title('图7-2 海风项目IRR对电价与利用小时的敏感性（示意模型）', fontsize=11)
ax.legend(fontsize=8.5, loc='lower right')
ax.grid(alpha=0.4, linestyle='--')
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(os.path.join(OUT, 'fig7-2_海风IRR敏感性.png')); plt.close()

print('charts b3 done:', os.listdir(OUT))
