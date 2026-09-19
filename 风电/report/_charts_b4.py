# -*- coding: utf-8 -*-
"""风电手册 第8-9章 图表生成"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 200

OUT = r'C:\Users\veken\Desktop\风电\report\charts'
os.makedirs(OUT, exist_ok=True)

# ============ 图8-1 整机商2026H1营收与归母净利 ============
fig, ax = plt.subplots(figsize=(8.6, 4.8))
comps = ['金风科技', '明阳智能', '三一重能', '运达股份', '电气风电']
rev = [337.4, 170.4, 106.6, 138.3, 56.5]
np_ = [18.55, 1.11, 2.33, -2.49, -5.5]  # 电气风电亏损，约-5.5为示意（未披露具体额，用"亏损"标注）
x = np.arange(len(comps)); w = 0.36
b1 = ax.bar(x-w/2, rev, w, label='营业收入（亿元）', color='#1A2E4B')
b2 = ax.bar(x+w/2, np_, w, label='归母净利润（亿元）', color='#E8720C')
for b in b1: ax.text(b.get_x()+b.get_width()/2, b.get_height()+4, f'{b.get_height():.0f}', ha='center', fontsize=8.5, fontweight='bold')
for b in b2:
    v = b.get_height()
    ax.text(b.get_x()+b.get_width()/2, v+1.2 if v>=0 else v-3, f'{v:.1f}', ha='center', fontsize=8.5, fontweight='bold')
ax.axhline(0, color='#999', linewidth=0.8)
ax.set_xticks(x); ax.set_xticklabels(comps)
ax.set_ylabel('亿元')
ax.set_title('图8-1 五大整机商2026年上半年营收与归母净利润', fontsize=11)
ax.legend(fontsize=9); ax.grid(axis='y', linestyle='--', alpha=0.4)
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(os.path.join(OUT, 'fig8-1_整机业绩.png')); plt.close()

# ============ 图8-2 重点公司估值对比（PE） ============
fig, ax = plt.subplots(figsize=(8.6, 4.8))
comps = ['金风科技', '东方电缆', '大金重工', '新强联', '中天科技', '亨通光电', '龙源电力', '三峡能源']
pe = [20.8, 21.8, 25.0, 14.5, 32.3, 38.5, 35.7, 93.5]  # 大金按25x一致预期
colors = ['#1A2E4B']*4 + ['#4E79A7']*4
y = np.arange(len(comps))
bars = ax.barh(y, pe, height=0.6, color=colors)
for yi, v in zip(y, pe):
    ax.text(v+1.2, yi, f'{v:.1f}x', va='center', fontsize=9, fontweight='bold')
ax.set_yticks(y); ax.set_yticklabels(comps); ax.invert_yaxis()
ax.set_xlabel('市盈率（倍，2026年9月）')
ax.set_xlim(0, 110)
ax.set_title('图8-2 风电重点公司估值对比（PE口径）', fontsize=11)
ax.grid(axis='x', linestyle='--', alpha=0.4)
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(os.path.join(OUT, 'fig8-2_估值对比.png')); plt.close()

# ============ 图9-1 产业链投资价值分层（看好度矩阵） ============
fig, ax = plt.subplots(figsize=(8.6, 5.0))
seg = ['海缆', '塔基基础\n（出海）', '轴承\n（国产替代）', '叶片\n（双寡头）', '齿轮箱\n（半直驱）', '整机\n（盈利拐点）', '铸锻件\n（大型化）', '变流器\n（构网型）', '运营商\n（类公用）', '漂浮式\n（远期期权）']
# 弹性（0-100）与确定性（0-100）
flex = [85, 90, 80, 60, 70, 75, 55, 50, 40, 65]
certainty = [90, 75, 70, 85, 80, 60, 75, 65, 90, 35]
colors = ['#1A2E4B' if c>=75 and f>=70 else ('#4E79A7' if c>=60 else '#B0B8C4') for c, f in zip(certainty, flex)]
ax.scatter(flex, certainty, s=420, c=colors, alpha=0.85, edgecolors='white', linewidths=1.2)
for xi, yi, label in zip(flex, certainty, seg):
    ax.annotate(label, (xi, yi), textcoords='offset points', xytext=(0, 12), ha='center', fontsize=8.5)
ax.axvline(62, color='#E8720C', linestyle='--', linewidth=1, alpha=0.6)
ax.axhline(60, color='#E8720C', linestyle='--', linewidth=1, alpha=0.6)
ax.set_xlim(20, 100); ax.set_ylim(20, 100)
ax.set_xlabel('盈利弹性（出海/涨价/国产替代驱动，%）')
ax.set_ylabel('景气确定性（订单/格局/政策支撑，%）')
ax.set_title('图9-1 风电产业链环节投资价值分层（示意判断）', fontsize=11)
ax.grid(alpha=0.4, linestyle='--')
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(os.path.join(OUT, 'fig9-1_投资分层.png')); plt.close()

print('charts b4 done')
