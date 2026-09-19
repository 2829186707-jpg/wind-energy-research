# -*- coding: utf-8 -*-
"""风电手册 第3-5章 图表生成"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 200

OUT = r'C:\Users\veken\Desktop\风电\report\charts'
os.makedirs(OUT, exist_ok=True)

# ============ 图3-1 中国风电年新增装机路径 ============
fig, ax = plt.subplots(figsize=(8.2, 4.6))
years = ['2025A', '2026E', '十五五年均']
land = [93.4, 105, 105]      # 陆风：2025约100-6.6=93.4；2026E陆约110-120取中105；十五五120-15=105
sea  = [6.6, 10, 15]         # 海风：2025实际6.6；2026E 8-10取10；十五五年均15
x = range(len(years))
b1 = ax.bar(x, land, width=0.5, label='陆上风电', color='#1A2E4B')
b2 = ax.bar(x, sea, width=0.5, bottom=land, label='海上风电', color='#4E79A7')
for i in x:
    ax.text(i, land[i]+sea[i]+2, f'{land[i]+sea[i]:.1f}', ha='center', fontsize=10, fontweight='bold')
    ax.text(i, land[i]/2, f'陆{land[i]:.0f}', ha='center', va='center', color='white', fontsize=9)
    ax.text(i, land[i]+sea[i]/2, f'海{sea[i]:.0f}', ha='center', va='center', color='white', fontsize=9)
ax.set_xticks(list(x)); ax.set_xticklabels(years)
ax.set_ylabel('年新增装机（GW）')
ax.set_ylim(0, 145)
ax.set_title('图3-1 中国风电年新增装机结构（2025实际/2026预计/十五五年均）', fontsize=11)
ax.legend(loc='upper left', fontsize=9)
ax.grid(axis='y', linestyle='--', alpha=0.4)
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(os.path.join(OUT, 'fig3-1_装机路径.png')); plt.close()

# ============ 图3-2 全球海上风电新增装机预测 ============
fig, ax = plt.subplots(figsize=(8.2, 4.2))
years = ['2025A', '2026E', '2028E', '2030E']
vals = [9.3, 13, 22, 33]   # GWEC：9.3→33GW，中间年份为线性示意
bars = ax.bar(years, vals, width=0.5, color='#1A2E4B')
for b, v in zip(bars, vals):
    ax.text(b.get_x()+b.get_width()/2, v+0.8, f'{v}', ha='center', fontsize=10, fontweight='bold')
ax.set_ylabel('全球海风年新增并网（GW）')
ax.set_ylim(0, 40)
ax.set_title('图3-2 全球海上风电年新增装机预测（GWEC）', fontsize=11)
ax.grid(axis='y', linestyle='--', alpha=0.4)
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(os.path.join(OUT, 'fig3-2_全球海风预测.png')); plt.close()

# ============ 图4-1 陆上整机成本构成 ============
fig, ax = plt.subplots(figsize=(8.2, 4.6))
labels = ['叶片', '齿轮箱', '塔筒', '发电机', '轴承', '变流器', '其他']
lo = [20, 12, 10, 8, 5, 4.8, 10]
hi = [25, 15, 12, 10, 7, 6, 15]
mid = [(a+b)/2 for a, b in zip(lo, hi)]
y = range(len(labels))
ax.barh(y, [b-a for a, b in zip(lo, hi)], left=lo, height=0.55, color='#4E79A7', alpha=0.75)
for yi, m in zip(y, mid):
    ax.text(m, yi, f'{m:.1f}%', ha='center', va='center', fontsize=9, fontweight='bold', color='white')
ax.set_yticks(list(y)); ax.set_yticklabels(labels)
ax.invert_yaxis()
ax.set_xlabel('占整机成本比重（%）')
ax.set_xlim(0, 30)
ax.set_title('图4-1 陆上风电机组成本构成区间（行业口径）', fontsize=11)
ax.grid(axis='x', linestyle='--', alpha=0.4)
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(os.path.join(OUT, 'fig4-1_整机成本构成.png')); plt.close()

# ============ 图4-2 主轴轴承国产化率与TRB渗透率 ============
fig, ax = plt.subplots(figsize=(8.2, 4.4))
import numpy as np
cats = ['2024', '2025', '2026E']
local = [63.2, 70.5, 78]      # 主轴轴承国产化率
trb = [10, 40, 62]            # TRB渗透率（不足10%→40%→55-70%中值）
x = np.arange(len(cats)); w = 0.35
b1 = ax.bar(x-w/2, local, w, label='主轴轴承国产化率（%）', color='#1A2E4B')
b2 = ax.bar(x+w/2, trb, w, label='TRB结构渗透率（%）', color='#E8720C')
for b in b1: ax.text(b.get_x()+b.get_width()/2, b.get_height()+1.5, f'{b.get_height():.0f}', ha='center', fontsize=9, fontweight='bold')
for b in b2: ax.text(b.get_x()+b.get_width()/2, b.get_height()+1.5, f'{b.get_height():.0f}', ha='center', fontsize=9, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(cats)
ax.set_ylim(0, 95); ax.set_ylabel('占比（%）')
ax.set_title('图4-2 风电主轴轴承国产化率与TRB渗透率提升路径', fontsize=11)
ax.legend(fontsize=9); ax.grid(axis='y', linestyle='--', alpha=0.4)
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(os.path.join(OUT, 'fig4-2_轴承国产化.png')); plt.close()

# ============ 图5-1 2025年国内陆上风机新增装机份额 ============
fig, ax = plt.subplots(figsize=(8.2, 4.6))
comps = ['金风科技', '运达股份', '明阳智能', '远景能源', '三一重能', '中国中车', '东方电气', '电气风电', '中船海装', '其他']
shares = [19.0, 15.3, 13.7, 13.5, 11.6, 9.8, 9.3, 4.4, 3.2, 0.2]
colors = ['#1A2E4B']*5 + ['#4E79A7']*4 + ['#B0B8C4']
y = range(len(comps))
ax.barh(y, shares, height=0.6, color=colors)
for yi, s in zip(y, shares):
    ax.text(s+0.3, yi, f'{s}%', va='center', fontsize=9, fontweight='bold')
ax.set_yticks(list(y)); ax.set_yticklabels(comps); ax.invert_yaxis()
ax.set_xlabel('份额（%）'); ax.set_xlim(0, 22)
ax.set_title('图5-1 2025年国内陆上风机新增装机份额（平安证券口径）', fontsize=11)
ax.grid(axis='x', linestyle='--', alpha=0.4)
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(os.path.join(OUT, 'fig5-1_整机份额.png')); plt.close()

# ============ 图5-2 2026H1 国内整机中标TOP + 风电整机净利 ============
fig, ax = plt.subplots(figsize=(8.2, 4.4))
comps = ['金风科技', '运达股份', '远景能源', '明阳智能', '其他']
gw = [10.1, 9.33, 8.28, 8.0, 27.0]
colors = ['#1A2E4B', '#2F4A3B', '#4E79A7', '#5A8FB8', '#B0B8C4']
bars = ax.bar(comps, gw, width=0.5, color=colors)
for b, v in zip(bars, gw):
    ax.text(b.get_x()+b.get_width()/2, v+0.4, f'{v}', ha='center', fontsize=9, fontweight='bold')
ax.set_ylabel('中标规模（GW）')
ax.set_ylim(0, 12)
ax.set_title('图5-2 2026年上半年国内风电整机中标格局（TOP4+其他）', fontsize=11)
ax.grid(axis='y', linestyle='--', alpha=0.4)
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.subplots_adjust(left=0.12, right=0.97, top=0.88, bottom=0.18)
plt.savefig(os.path.join(OUT, 'fig5-2_2026H1中标.png')); plt.close()

print('charts done:', os.listdir(OUT))
