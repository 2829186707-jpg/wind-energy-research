# -*- coding: utf-8 -*-
p = r'D:\桌面\风电\风电\report\_gen_report.py'
with open(p, 'r', encoding='utf-8') as f:
    s = f.read()

# 1) chain-items 改 4 列网格
old_ci = ".chain-items{display:flex;flex-wrap:wrap;gap:8px;padding:12px 16px}"
new_ci = ".chain-items{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:12px 16px}"
assert old_ci in s
s = s.replace(old_ci, new_ci)

# 移动端补 2 列
old_m = "@media(max-width:768px){.section{padding:20px 14px}"
new_m = "@media(max-width:768px){.chain-items{grid-template-columns:repeat(2,1fr)}.section{padding:20px 14px}"
assert old_m in s
s = s.replace(old_m, new_m)

# 2) 第六章末尾加 6.3 + canvas
old_62_end = """整机龙头的盈利弹性与估值修复空间被低估，这是2026-2027年风电板块最重要的投资判断之一。</p>
''')"""
new_62_end = """整机龙头的盈利弹性与估值修复空间被低估，这是2026-2027年风电板块最重要的投资判断之一。</p>
<h3>6.3 盈利敏感性热力图：招标价×原材料成本</h3>
<p>整机商净利率对两大变量高度敏感：招标均价（收入端）与钢材/玻纤/铜/稀土等原材料成本（成本端）。以2026年基准净利率约**4%**为锚，招标价每变动**±15%**约带动净利率**±5个百分点**，原材料综合成本每变动**±20%**约反向带动净利率**±5个百分点**。热力图显示：在"招标价持平+成本上行10%"的中性偏空组合下整机净利率仅约**1.5%**，而"招标价+7.5%+成本-10%"的改善组合下净利率可达**9.1%**——这正是市场定价分化的根源，也是跟踪招标价企稳与原材料价格的核心意义。</p>
<div class="fig-chart" id="chart-sens"></div>
<div class="fig-cap">图6-2 整机商净利率对招标均价与原材料成本变动的敏感性（示意模型，基准净利率4%）· 点击色块查看组合解读</div>
''')"""
assert old_62_end in s
s = s.replace(old_62_end, new_62_end)

# 3) CHART_JS2 加 c10 heatmap
old_resize = "[c1,c2,c3,c4,c5,c6,c7,c8,c9].forEach(function(c){c.resize();});});"
new_c10 = """
var c10=echarts.init(gd('chart-sens'));
var sx=['-15%','-7.5%','持平','+7.5%','+15%'];
var sy=['-20%','-10%','持平','+10%','+20%'];
var sm=[[3.8,6.4,9.0,11.6,14.3],[1.3,3.9,6.5,9.1,11.8],[-1.3,1.4,4.0,6.6,9.3],[-3.8,-1.1,1.5,4.1,6.8],[-6.3,-3.6,-1.0,1.6,4.3]];
var sd=[];
for(var yi=0;yi<5;yi++){for(var xi=0;xi<5;xi++){sd.push([xi,yi,sm[yi][xi]]);}}
c10.setOption({
tooltip:{position:'top',formatter:function(p){return '招标价'+sx[p.data[0]]+' · 原材料成本'+sy[p.data[1]]+'<br/>整机净利率约：<b>'+p.data[2]+'%</b>';},backgroundColor:'#252836',borderColor:'#3b82f6',textStyle:{color:'#e4e6eb'}},
grid:{left:'14%',right:'10%',top:'8%',bottom:'16%'},
xAxis:{type:'category',data:sx,name:'招标均价变动',nameLocation:'middle',nameGap:30,nameTextStyle:{color:'#9aa1b2'},axisLabel:{color:'#9aa1b2'},splitArea:{show:true}},
yAxis:{type:'category',data:sy,name:'原材料成本变动',nameTextStyle:{color:'#9aa1b2'},axisLabel:{color:'#9aa1b2'},splitArea:{show:true}},
visualMap:{min:-7,max:15,calculable:true,orient:'horizontal',left:'center',bottom:0,inRange:{color:['#ef4444','#f59e0b','#22c55e']},textStyle:{color:'#9aa1b2'}},
series:[{type:'heatmap',data:sd,label:{show:true,color:'#0f1117',fontWeight:'bold',fontSize:12},emphasis:{itemStyle:{shadowBlur:10,shadowColor:'rgba(0,0,0,0.5)'}}}]
});
c10.on('click',function(p){var m=p.data;var txt='<p><b>招标均价'+sx[m[0]]+'，原材料综合成本'+sy[m[1]]+'</b></p><p>该组合下整机商净利率约 <b>'+m[2]+'%</b>。'+(m[2]>=8?'盈利显著改善，对应招标价企稳+成本下行双击的乐观情形。':(m[2]>=2?'盈利微利至正常，为基准偏中性情形。':(m[2]>=0?'接近盈亏平衡，价格战尾部情形。':'净利率为负，整机厂亏损，对应价格战深度出清阶段。')))+'</p><p class="fig-note">模型为示意：基准净利率4%，招标价弹性约±0.35pct/1%，成本弹性约∓0.25pct/1%。</p>';openModal('盈利敏感性组合','整机净利率 '+m[2]+'%',txt);});
window.addEventListener('resize',function(){[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10].forEach(function(c){c.resize();});});});"""
assert old_resize in s
s = s.replace(old_resize, new_c10)

# 4) 第九章 9.2 文字改表格
old_92 = """<h3>9.2 跟踪指标清单</h3>
<p>按重要性排序：月度风电装机/并网数据（国家能源局）、风机招标量（风电头条/北极星）、整机中标价格（含塔筒/不含塔筒）、海风开工与吊装进度（船机利用）、海缆中标与订单（东方/中天公告）、欧洲海风招标与单桩价格、原材料价格（钢材/玻纤/稀土/铜）、运营商IRR与电价竞价结果。</p>"""
new_92 = """<h3>9.2 跟踪指标清单</h3>
<p class="tbl-title">表9-1 风电板块核心跟踪指标与验证信号</p>
<div class="tbl-wrap"><table>
<tr><th>指标</th><th>数据来源</th><th>验证信号（看多阈值）</th></tr>
<tr><td>月度新增装机/并网</td><td>国家能源局</td><td>2026年全年≥120GW、海风月吊装≥1GW</td></tr>
<tr><td>风机招标量</td><td>风电头条/北极星</td><td>年度招标≥110GW，领先装机1.5-2年</td></tr>
<tr><td>整机中标均价</td><td>招标公示</td><td>陆风不含塔筒站稳1600元/kW不再下行</td></tr>
<tr><td>海风开工与吊装</td><td>船机/施工公告</td><td>WTIV利用率提升、月度吊装放量</td></tr>
<tr><td>海缆中标/订单</td><td>东方电缆/中天科技公告</td><td>在手订单环比增长、500kV级中标</td></tr>
<tr><td>欧洲海风招标/单桩价格</td><td>GWEC/欧洲招标平台</td><td>欧洲单桩招标价、中国企业中标份额</td></tr>
<tr><td>原材料价格</td><td>钢联/百川</td><td>钢材/玻纤/稀土/铜价格不出现单边上涨</td></tr>
<tr><td>运营商IRR与电价竞价</td><td>项目公示/电力交易中心</td><td>机制电价竞价结果不低于预期、IRR≥6.5%</td></tr>
</table></div>"""
assert old_92 in s
s = s.replace(old_92, new_92)

with open(p, 'w', encoding='utf-8') as f:
    f.write(s)
print('ALL PATCHED')
