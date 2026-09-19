# -*- coding: utf-8 -*-
"""风电行业研究·研报网页生成器 v3：ECharts 交互图表 + 数据标红 + 统一配色"""
import os
import json

OUT = r'D:\桌面\风电\风电\report\index.html'

def mark_parse(s):
    parts = s.split('**')
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append('<mark>' + part + '</mark>')
        else:
            out.append(part)
    return ''.join(out)

S = {}

S['summary'] = ('核心摘要', '''
<h1>风电行业研究</h1>
<h2>核心结论摘要</h2>
<div class="grid grid-3">
<div class="card metric"><div class="metric-value">1.2亿kW</div><div class="metric-label">2026年风电新增装机预测</div></div>
<div class="card metric"><div class="metric-value">169GW</div><div class="metric-label">2025年全球风电新增（+38%）</div></div>
<div class="card metric"><div class="metric-value">1595元/kW</div><div class="metric-label">陆风整机中标均价（企稳）</div></div>
<div class="card metric"><div class="metric-value">105-120GW</div><div class="metric-label">“十五五”陆风年新增中枢</div></div>
<div class="card metric"><div class="metric-value">8-10GW</div><div class="metric-label">2026年海上风电新增（+30%）</div></div>
<div class="card metric"><div class="metric-value">1500万kW</div><div class="metric-label">“十五五”海风年新增目标·2030累计1亿kW+</div></div>
</div>
<div class="conclusion">
<h4>核心结论</h4>
<ul>
<li><strong>行业定位：量增价稳的景气上行期。</strong>2026年中国风电新增装机约**1.2亿**千瓦，全球新增**169GW**连续第三年刷新纪录；整机价格连续多月在**1600元/kW**附近企稳，海风进入放量前夜，产业链盈利拐点初现。</li>
<li><strong>三大主线：海风放量、出海、盈利修复。</strong>“十五五”海风年新增不低于**1500万千瓦**（2030年累计**1亿千瓦**以上）；海外市场毛利率高**5-15pct**，中国企业订单排至2027-2028年；整机价格企稳+结构升级带来盈利修复弹性。</li>
<li><strong>环节选择：格局与出海决定弹性。</strong>海缆（三强垄断）、塔基基础（出海+自有运力）、轴承（国产替代）是格局最优环节；整机龙头盈利修复弹性最大；纯陆风二线无出海能力的厂商持续承压。</li>
</ul>
</div>
<div class="grid grid-3">
<div class="card card-highlight"><h3>看好方向</h3><p>海缆（东方电缆/中天科技/亨通光电）——格局最优、高压壁垒、深远海量价齐升；塔基基础出海（大金重工/天顺风能）——欧洲缺口+自有运力+毛利率**35%+**；轴承国产替代（新强联）——TRB渗透率**70%+**、齿轮箱轴承**129亿**市场；整机龙头盈利修复（金风科技/三一重能）——价格企稳、海风放量与出海兑现；叶片双寡头（中材科技/时代新材）——格局稳、碳纤维升级、海外订单</p></div>
<div class="card card-warning"><h3>持有方向</h3><p>风电运营商（龙源电力/三峡能源/中广核新能源）——类公用事业属性，股息率与装机成长为锚，适合作为组合基础配置；金风科技等盈利确定性龙头——盈利修复与估值修复的确定性标的</p></div>
<div class="card card-danger"><h3>回避方向</h3><p>无出海能力、无海风业绩的纯陆风二三线整机/零部件厂商（价格战+份额流失双重挤压）；仅蹭风电概念而无订单验证的公司；高估值且盈利持续亏损的整机商；过度依赖补贴退坡前抢装逻辑的环节</p></div>
</div>
''')

S['macro'] = ('一、宏观趋势', '''
<h2>一、宏观趋势：全球与中国装机空间</h2>
<h3>1.1 全球装机：从百GW到太瓦时代</h3>
<p>全球风电在2025年创下历史纪录。据彭博新能源财经《2025年全球风电整机制造商市场份额》，2025年全球风电新增装机**169GW**、同比增长**38%**，连续第三年刷新纪录；其中陆上**161GW**（占比95%）、海上**8GW**。全球风能理事会（GWEC）口径下，2025年全球海上风电新增并网**9.3GW**、同比增长**16%**，为历史第三高年度，累计装机**92.5GW**，逼近100GW里程碑；中国以**6.6GW**新增海风连续第八年位居全球第一。GWEC预测，全球海上风电年新增装机将从2025年的**9.3GW**增至2030年的**33GW**，海风在风电新增中的占比将从6%提升至**16%**；2030年前全球风电累计装机有望突破**2TW**。</p>
<p>中国是绝对主力。**2025年中国是全球首个单个年新增装机突破100GW的风电市场**；水电水利规划设计总院《中国可再生能源发展报告2025年度》预计，2026年中国风电新增并网约**1亿千瓦**；中国可再生能源学会风能专业委员会预计2026年风电新增装机约**1.2亿千瓦**。分结构看，已完成机制电价竞价的省份2026年风电装机规模预计**8513万千瓦**，其中纳入机制电价的项目约**7009万千瓦**。</p>
<p>把时间轴拉长，“十五五”的目标体系已经清晰：《风能北京宣言2.0》（2025年10月）提出“十五五”期间中国风电年新增装机不低于**1.2亿千瓦**，其中海上风电年新增不低于**1500万千瓦**；2030年累计装机**13亿千瓦**、2035年不少于**20亿千瓦**、2060年达**50亿千瓦**。《可再生能源发展“十五五”规划》进一步明确，全国海上风电新增开工规模**1亿千瓦**左右、2030年累计并网**1亿千瓦**以上。这意味着未来五年中国风电年新增装机维持在1.2亿千瓦上下，是2020年（约7200万千瓦）的**1.7倍**量级，行业天花板远未到来。</p>
<p class="tbl-title">表1-1 全球与中国风电装机关键坐标（2025-2030）</p>
<div class="tbl-wrap"><table>
<tr><th>口径</th><th>2025年实际</th><th>2026年预计</th><th>2030年目标</th></tr>
<tr><td>全球新增（GWEC/BNEF）</td><td>169GW（海风9.3GW）</td><td>—</td><td>海风年新增33GW</td></tr>
<tr><td>中国新增（水电总院/风能专委会）</td><td>超100GW（全球首个）</td><td>约1-1.2亿千瓦</td><td>—</td></tr>
<tr><td>中国海风年新增</td><td>6.6GW（全球第一）</td><td>8-10GW（同比+30%）</td><td>不低于1500万千瓦</td></tr>
<tr><td>中国累计装机</td><td>—</td><td>约6.5-6.6亿千瓦</td><td>13亿千瓦</td></tr>
<tr><td>中国海风累计</td><td>0.47亿千瓦</td><td>—</td><td>1亿千瓦以上</td></tr>
</table></div>
<h3>1.2 风电与光伏：定位差异与互补</h3>
<p>新能源投资中风电与光伏的选择，关键在于识别两者的本质差异。第一，出力特性：风电利用小时数高（陆上约**2200-2400**小时、海上约**3000-3800**小时），光伏普遍在**1200-1600**小时，风电出力更平稳，接近可调电源；第二，资源约束：光伏受土地与消纳约束更明显，风电受风资源与电网送出约束，海风可大规模离岸布置、不占土地；第三，产业成熟度：光伏已深度内卷、组件价格战多年，风电大型化带来的降本仍在释放，海风产业链仍在放量与技术升级并行阶段；第四，政策定位：光伏在户用与分布式市场更灵活，风电在大基地与深远海具备不可替代性。</p>
<p>对投资而言，风电与光伏互补大于互斥：风电大基地通常配套储能、配电网送出，风电的稳定出力提升了整体项目的消纳质量；而在同一场址上，海上风电与海上光伏还出现风光同场的融合开发模式，两者共享送出通道与运维体系，进一步摊薄单位成本。</p>
<h3>1.3 度电成本：风电已是成本最低的新能源之一</h3>
<p>风电的长期需求来自经济性。过去十年，全球陆上风电度电成本（LCOE）下降约**50%-60%**，海上风电近五年下降约**30%-40%**，核心是风机大型化（单机容量从2MW提升至**6-10MW**，海风已达**18-20MW**级）、产业链规模化与施工效率提升。当前中国陆上风电已全面实现平价上网，新建风电项目度电成本普遍低于当地煤电基准价（陆风约**0.15-0.25元/kWh**、海风约**0.3-0.4元/kWh**）；海上风电在近海浅水区基本达到平价临界点，2026年海风招标中标均价约**3280元/kW**，配合大型化与施工效率提升，深远海项目的经济性正在逐步改善。</p>
<h3>1.4 中国风电的全球定价权与出海</h3>
<p>中国是全球风电制造中心，**产业链产值占全球70%以上**；整机、叶片、塔筒、齿轮箱、铸件等环节的中国产能均为全球最大，制造成本比欧洲低**30%-50%**。这种成本优势正在转化为出口份额。整机端，远景2025年全球吊装突破**20GW**，海外吊装**4.8GW**（同比**+15倍**）；金风、明阳、运达、三一均在欧洲、中亚、中东、东南亚布局。零部件端，塔筒、法兰、海缆、铸件等环节已深度嵌入全球供应链，东方电缆、中天科技、亨通光电的海缆进入欧洲市场，大金重工、天顺风能承接海外塔筒与桩基订单。</p>
<p>海外订单毛利率通常高于国内**5-15个百分点**，且以欧元、美元计价，汇率友好；国内价格战压制盈利时，出海比例提升可直接改善综合毛利率，是2026-2027年盈利与估值改善的重要方向。</p>
''')
S['policy'] = ('二、政策与商业模式', '''
<h2>二、政策与商业模式：电价机制演变与收入结构</h2>
<h3>2.1 补贴退坡史：从标杆电价到平价时代</h3>
<p>中国风电电价机制经历了四个阶段。第一阶段（**2009-2020年**）标杆上网电价时代：按资源区划定**0.29-0.57元/kWh**不等的标杆电价，叠加国家补贴，催生2015年、2020年两轮陆上抢装潮；第二阶段（**2021年**）平价元年：陆上风电国家补贴正式退出，新建项目执行燃煤基准价；第三阶段（**2022-2025年**）竞争性配置与市场化交易并行：部分省份以竞价方式分配指标，风电市场化交易电量占比快速提升；第四阶段（**2026年**）全面入市：136号文落地，新能源上网电价全面由市场形成。</p>
<p>补贴退坡的直接结果是行业从政策驱动切换为成本与收益驱动：装机节奏不再由抢装节点决定，而是由项目IRR与电网消纳能力决定。2022-2024年招标量高增但装机波动，原因是开发商在等电价明确、等风机价格企稳。2026年是商业模式的分水岭。</p>
<h3>2.2 136号文：新能源全面入市</h3>
<p>**2025年**发布的136号文（《关于深化新能源上网电价市场化改革促进新能源高质量发展的通知》）是近年来风电领域最重要的政策，核心是存量项目机制电价衔接、增量项目全面入市。存量项目：按现有机制与电价结算方式执行，逐步过渡；增量项目（**2026年起投产**）：不再安排固定电价，通过机制电价形成差价结算，其余电量进入电力市场按现货/中长期价格结算。</p>
<p>对风电商业模式的影响体现在四个层面。第一，收益确定性下降：电价从“锁定”变为“市场波动”，项目IRR的敏感性显著上升；第二，优质资源向高效开发商集中：机制电价竞价考验开发商对风资源、成本与市场的综合判断，拥有低成本与精细化运营能力的央企（三峡、中广核新能源等）优势扩大；第三，推动电、储与环境溢价的多元收入：绿电交易、绿证、CCER成为弥补市场化电价下行的重要抓手；第四，产业链资本压力下行业出清，大型化、构网型风机与高效海缆等技术的价值进一步凸显。</p>
<h3>2.3 机制电价竞价、绿电交易与CCER</h3>
<p>机制电价是136号文的核心配套工具：地方政府对增量风电项目组织竞价，竞价结果决定项目可获得的机制电价水平与对应的价差结算量。2026年已完成机制电价竞价的省份，纳入机制电价的风电规模约**7000万千瓦**，相当于锁定了电价下限，是未来两年最确定的装机底盘。绿电交易方面，风电绿电价格在部分省份可达**0.03-0.08元/kWh**，叠加绿证收入，可在一定程度上对冲市场化电价下行；CCER（国家核证自愿减排量）重启后，平价风电项目的碳资产收益逐步被市场定价，构成运营收入的补充项。</p>
<p>风电运营收入由电价、机制价差与绿电/CCER溢价构成。136号文后电价全面入市，电价假设成为项目IRR测算的最大不确定性——电价每低**0.02元/kWh**，IRR约下降**1.5个百分点**；利用小时每降**200小时**，IRR约下降**1个百分点**。这也是市场对海风项目评估存在分歧的原因。</p>
<h3>2.4 以大代小与千乡万村驭风：存量市场的新增量</h3>
<p>在新建装机之外，存量改造正成为风电需求的重要补充。中国早期安装的风机单机容量小（**1.5MW**以下）、运行效率低，大批机组进入**15-20年**寿命周期，具备以大代小改造价值——用**4-6MW**新机组替换老旧机组，在相同机位下容量可提升**2-4倍**、利用小时数提升**30%以上**。2026年以来中能院、国家能源集团等央企全面启动“以大代小”技改增容指标，十五五期间存量改造年化贡献约**10-20GW**增量。</p>
<p>千乡万村驭风行动打开分散式风电空间：在广大农村地区利用零散土地安装小容量风机，就近消纳、就地并网，**2026年**已成为整机商重要订单来源（金风科技在河北、内蒙古等地斩获多个分散式项目）。叠加以旧换新政策对老旧风机的置换补贴，存量市场为整机与零部件企业提供了穿越新建装机波动的补充。</p>
<h3>2.5 运营商业模式：电价×利用小时×IRR</h3>
<p>风电运营是典型的重资产、现金流型生意，收入=装机容量×利用小时×上网电价，成本以折旧（占比约**40%-50%**）与运维为主，边际成本极低。运营商的盈利弹性主要来自三处：利用小时提升（风资源评估、智能运维）、电价结构优化（绿电交易溢价提升）、财务费用下降（利率下行周期中高杠杆项目的利息释放）。</p>
<p>IRR视角下，典型陆上风电项目全投资IRR约**6%-10%**，海上风电项目约**6%-8%**（近海、大型化后向**8%-10%**改善）；136号文后电价市场化使IRR对电价假设的敏感性显著上升，优质项目（高风速+低造价+高绿电溢价）与普通项目的回报分化拉大。运营环节的代表公司包括龙源电力、三峡能源、中广核新能源、节能风电等，其估值逻辑更接近公用事业，兼有资产期权属性：股息率与成长是核心，绿电、CCER是估值弹性。</p>
''')

S['demand'] = ('三、需求测算', '''
<h2>三、需求测算：十五五装机空间拆解</h2>
<h3>3.1 陆风：每年105-120GW的构成拆解</h3>
<p>陆上风电是装机的绝对主体，占新增总量的**85%-90%**。2026年行业主流预测集中在**110-120GW**：水电水利规划设计总院预计2026年风电新增并网约**1亿千瓦**（口径偏保守）；华泰证券预计2026年国内新增装机**130GW**（其中陆风120GW、海风10GW）；中国可再生能源学会风能专委会预计2026年风电新增装机约**1.2亿千瓦**。综合各口径，2026-2030年陆风年新增中枢约**105-120GW**，是2020年（约7200万千瓦）的**1.5-1.7倍**。</p>
<p>陆风的需求并非单一来源，而是由四类项目池构成，每一类的驱动逻辑不同。第一，沙戈荒大基地：这是“十四五”末期与“十五五”的主体，单项目规模动辄GW级，集中在新疆、内蒙古、甘肃、青海等“三北”地区，2026年一季度“三北”地区贡献了全国**75%**的新增装机；第二，分散式与“千乡万村驭风”：利用零散土地就近开发，2026年以来金风、运达、远景等均在河北、内蒙古、青海等地斩获多个分散式项目，边际贡献快速提升；第三，存量技改“以大代小”：用**4-6MW**新机组替换早期**1.5MW**以下老机组，同机位容量提升**2-4倍**、利用小时提升**30%以上**，“十五五”期间年化贡献约**10-20GW**；第四，常规平价与市场化项目：通过机制电价竞价获取指标的常规项目，是装机的基本盘。</p>
<p>判断陆风需求的核心领先指标是招标量。2026年一季度央国企风电项目整机集采定标累计约**56.93GW**；2026年1-8月央国企整机中标达**105.98GW**，已超过去年同期。高招标量为未来1-2年的装机提供确定性：风电从招标到并网通常有**12-24个月**周期，2026年招标量对应的是2027-2028年的装机兑现，可用招标量乘1.5-2年周期推算未来装机，判断当前高景气的持续性。</p>
<h3>3.2 海风：8-10GW到年均1500万千瓦的爬坡路径</h3>
<p>海上风电是“十五五”增量弹性最大的方向，也是产业链价值量最厚、壁垒最高的环节。2025年中国海风新增并网**6.6GW**，连续第八年全球第一；2026年行业预计新增**8-10GW**，同比增长**30%**以上；而《风能北京宣言2.0》提出十五五期间海风年新增不低于**1500万千瓦**（即15GW），《可再生能源发展十五五规划》提出十五五期间全国海风新增开工规模**1亿千瓦**左右、2030年累计并网**1亿千瓦**以上；对比2025年底累计**0.47亿千瓦**，意味着五年内海风累计装机要翻一倍。</p>
<p>海风放量的路径分三步：第一步是近海规模化，当前在建与已核准的近海项目（离岸**30-50公里**、水深**20-40米**）是2026-2028年的主力，单机容量已从**8MW**升级至**11-18MW**，2026年央国企海风招标单机最大**18MW**；第二步是深远海基地，面向渤海、黄海、东海、南海四大海域规划布局，重点推动一批深远海项目开工，这是十五五后半段的主要增量；第三步是漂浮式商业化起步，2026年国内正在推进“三峡领航号”（**16MW**）、“春风号”（**17MW**）、“图强号”（**20MW**）等大兆瓦漂浮式样机，一旦验证经济性，将打开水深**50米**以上、占中国海风资源约**70%**的深远海空间。</p>
<p>海风与陆风的本质差异在价值量与产业链：单GW海上风电投资是陆上的**2-3倍**（陆上约**45-55亿元/GW**、海上约**110-130亿元/GW**），其中塔基与基础（单桩/导管架）占**20%-25%**、海缆占**10%-15%**、整机占**35%-40%**、叶片占**10%-12%**。更高的投资强度意味着同样的装机增速下，海风对零部件企业的收入拉动显著大于陆风。</p>
<div class="fig-chart" id="chart-annual"></div>
<div class="fig-cap">图3-1 中国风电年新增装机结构（2025实际/2026预计/十五五年均）· 点击柱形查看当年明细</div>
<div class="fig-chart" id="chart-global-offshore"></div>
<div class="fig-cap">图3-2 全球海上风电年新增装机预测（GWEC口径）· 点击柱形查看当年预测</div>
<h3>3.3 全球出海：第二增长曲线的量级测算</h3>
<p>海外市场是中国风电制造业的重要增量。GWEC预计2030年前全球风电累计装机有望突破**2TW**；全球海上风电年新增装机将从2025年的**9.3GW**增至2030年的**33GW**，海风在新增装机中的占比从**6%**提升至**16%**。欧洲、亚太（越南、菲律宾、印度）、中东与中亚是主要增量市场，欧洲本土产能不足，大金重工在欧洲海风基础结构市场市占率达**29.1%**居首。</p>
<p>中国整机商的出海已经进入兑现期。远景能源2025年全球新增吊装量首次突破**20GW**，其中海外吊装**4.8GW**、同比激增**15倍**，创中国整机企业海外吊装历史纪录；金风科技2025年海外订单维持**10GW**以上量级，2026年上半年海外订单多于去年同期；明阳、运达、三一、东方风电均在欧洲、中亚、中东、东南亚布局并持续中标。从总量看，2025年国内整机商海外中标/吊装合计约**5-6GW**，若2026-2030年维持每年翻倍左右的增速，2030年出口装机有望达到**20-30GW**，相当于再造一个海外市场的新增装机量。</p>
<p>出海环节的利润弹性同样可观：海外整机与零部件毛利率普遍高于国内**5-15个百分点**（如出口欧洲的海上单桩毛利率**35%-39%**），且以欧元/美元计价，汇率与价格体系均优于国内。对零部件企业而言，海外订单毛利率高、供需缺口大，是2026-2027年业绩与估值改善较确定的方向。</p>
''')
S['chain'] = ('四、产业链全景', '''
<h2>四、产业链全景：环节穿透与格局分层</h2>
<p class="lead">风电产业链按整机、零部件、运营三层展开：整机占投资约**50%-60%**，其余为叶片、齿轮箱、轴承、铸锻件、塔筒、变流器等零部件；零部件环节普遍毛利率高于整机，且大兆瓦化与国产化率提升是贯穿所有环节的两条主线。</p>
<div class="chain-layer"><div class="chain-layer-title">第1层 · 叶片——价值量最大的单一零部件，双寡头格局</div>
<div class="chain-items">
<span class="chain-item">价值量：占整机成本**20%-25%**（陆上单GW约**3-4亿元**）</span><span class="chain-item">格局：中材科技（全球第一，国内**28.9%**）+时代新材（约**24%**）双寡头</span><span class="chain-item">毛利率：约**18.9%**（价格战下保持较高）</span><span class="chain-item chain-item-hot">预期差：碳纤维主梁渗透率提升+海外订单（欧洲订单增**30%**）</span>
</div></div>
<div class="chain-layer"><div class="chain-layer-title">第2层 · 齿轮箱——前三强集中，半直驱渗透加速</div>
<div class="chain-items">
<span class="chain-item">价值量：占整机成本**12%-15%**（单GW约**2-2.4亿元**）</span><span class="chain-item">格局：南高齿**23.4%**+采埃孚**22.7%**+重齿**20.6%**（前三强**66.7%**）</span><span class="chain-item">毛利率：约**25%-30%**</span><span class="chain-item chain-item-hot">预期差：半直驱渗透+大兆瓦海风齿轮箱溢价+海外主机厂采购放量</span>
</div></div>
<div class="chain-layer"><div class="chain-layer-title">第3层 · 轴承——国产化率78.4%后的第二成长曲线</div>
<div class="chain-items">
<span class="chain-item">价值量：占整机成本**5%-7%**（单GW约**0.8-1.1亿元**）</span><span class="chain-item">格局：新强联（TRB渗透率**70%+**）、洛轴、瓦轴</span><span class="chain-item">国产化：整体**78.4%**、偏航变桨**91.3%**、主轴**70.5%**</span><span class="chain-item chain-item-hot">预期差：齿轮箱轴承国产化（**129亿**市场，最大替代空间）</span>
</div></div>
<div class="chain-layer"><div class="chain-layer-title">第4层 · 铸锻件——大兆瓦产能成为硬门槛</div>
<div class="chain-items">
<span class="chain-item">价值量：占整机成本**5%-8%**（单GW约**0.8-1.3亿元**）</span><span class="chain-item">格局：日月股份（国内**35%**、全球**25-30%**）、吉鑫**15.7%**、金雷（主轴全球**25%**）</span><span class="chain-item">毛利率：约**20%-25%**</span><span class="chain-item chain-item-hot">预期差：海风大型化单GW价值量提升+海外出口+核电第二曲线</span>
</div></div>
<div class="chain-layer"><div class="chain-layer-title">第5层 · 塔筒与法兰——价值量第二，出海弹性最大</div>
<div class="chain-items">
<span class="chain-item">价值量：占整机成本**10%-12%**（单GW约**2-2.5亿元**）；海风塔筒+基础占**20%-30%**（单GW约**24-36亿元**）</span><span class="chain-item">格局：天顺**21.3%**、大金**17.3%**、泰胜**13.8%**（CR5约**55%-60%**）</span><span class="chain-item">出海：大金欧洲市占**29.1%**居首，自有船队**24艘**（合同**120亿**）</span><span class="chain-item chain-item-hot">预期差：欧洲缺口**3-5年**难解，订单排至2027-2028年，出口毛利率**35%+**</span>
</div></div>
<div class="chain-layer"><div class="chain-layer-title">第6层 · 变流器与电气系统——国产化+构网型的隐形升级</div>
<div class="chain-items">
<span class="chain-item">价值量：占整机成本**4.8%-6%**（单GW约**0.8-1亿元**）</span><span class="chain-item">格局：禾望电气、阳光电源为第三方龙头；金风/远景/明阳自研比例上升</span><span class="chain-item">趋势：构网型变流器成为“沙戈荒大基地”与新型电力系统标配</span><span class="chain-item chain-item-hot">预期差：构网型产品溢价+IGBT国产化与SiC渗透带来成本下行</span>
</div></div>
<div class="chain-layer"><div class="chain-layer-title">第7层 · 整机——格局、价格战与盈利拐点</div>
<div class="chain-items">
<span class="chain-item">格局：2025年份额金风**19.0%**、运达**15.3%**、明阳**13.7%**、远景**13.5%**、三一**11.6%**（CR5约**73.1%**）</span><span class="chain-item">价格：陆风不含塔筒**1595元/kW**连续多月企稳，海风含塔筒约**3280元/kW**</span><span class="chain-item">盈利：毛利率**10%-15%**，2026年头部集中修复（金风+东方电气占行业盈利**93%**）</span><span class="chain-item chain-item-hot">预期差：海风放量、出海兑现与价格企稳下的盈利修复</span>
</div></div>
<div class="chain-layer"><div class="chain-layer-title">第8层 · 海缆——高压垄断环节，格局最清晰</div>
<div class="chain-items">
<span class="chain-item">价值量：占海风单GW投资**10%-15%**（单GW约**12-18亿元**）</span><span class="chain-item">格局：中天**36%-38%**、东方电缆**25%**、亨通**18%**（三家具备**500kV**交付能力）</span><span class="chain-item">盈利：东方电缆海缆毛利率**33.36%**、在手订单**193亿**</span><span class="chain-item chain-item-hot">预期差：电压等级跃迁（66kV阵列→330kV送出→±525kV直流）带来单GW价值量跃升</span>
</div></div>
<div class="chain-layer"><div class="chain-layer-title">第9层 · 塔基基础（海风）——单桩/导管架，出海第一赛道</div>
<div class="chain-items">
<span class="chain-item">价值量：占海风单GW投资**20%-25%**（单GW约**24-36亿元**）</span><span class="chain-item">格局：大金重工（欧洲**29.1%**）、天顺风能、海力风电、泰胜风能</span><span class="chain-item">壁垒：万吨级单桩需深水码头+大型门式起重机，出口资质稀缺</span><span class="chain-item chain-item-hot">预期差：欧洲产能缺口与自有运力构成壁垒，单吨盈利上修</span>
</div></div>
<div class="chain-layer"><div class="chain-layer-title">第10层 · 施工安装与漂浮式——船机是瓶颈，漂浮式是期权</div>
<div class="chain-items">
<span class="chain-item">施工：占海风投资**10%-15%**，中国WTIV在册**42艘**，需新增**15-20艘**大吨位船</span><span class="chain-item">漂浮式：2026年样机验证（**16-20MW**），2028-2030年商业化打开深远海**70%**空间</span><span class="chain-item">受益：广州打捞局、中交系统、龙源振华（船）；亚星锚链（系泊）；东方电缆/中天（动态海缆）</span><span class="chain-item chain-item-hot">预期差：船机资源是海风装机的真正瓶颈，跟踪吊装进度比招标量更能反映真实放量</span>
</div></div>
<div class="conclusion">
<h4>核心判断</h4>
<ul>
<li>格局最好的环节：海缆（三强垄断）、叶片（双寡头）、轴承（国产替代加速）。</li>
<li>出海弹性最大的环节：塔基基础（大金/天顺）、海缆（东方/中天）、整机（金风/远景）。</li>
<li>盈利拐点弹性最大的环节：整机（价格企稳+海风放量）、齿轮箱轴承（国产化）。</li>
</ul>
</div>
''')

S['diagram'] = ('产业链图解', '''
<h2>产业链图解：陆上与海上风电结构拆解</h2>
<p class="lead">点击风机上任一部件，即可查看该环节分析；塔筒、单桩等装机环节为聚合标签，点击后可再细分（塔筒/法兰/单桩/导管架/陆上基础）。</p>
<div class="diagram-wrap">
<div class="diagram-card">
<h3>陆上风电</h3>
<div class="fig-box">
<img src="assets/land.jpg" alt="陆上风电">
<svg viewBox="0 0 1000 1250" class="ov">
<g class="hp" onclick="openPart('blade')"><title>叶片</title><rect class="pill" x="652" y="166" width="96" height="28" rx="14"/><text class="lbl" x="700" y="185">叶片</text></g>
<g class="hp" onclick="openPart('gearbox')"><title>齿轮箱</title><rect class="pill" x="383" y="518" width="114" height="28" rx="14"/><text class="lbl" x="440" y="537">齿轮箱</text></g>
<g class="hp" onclick="openPart('bearing')"><title>轴承</title><rect class="pill" x="457" y="518" width="96" height="28" rx="14"/><text class="lbl" x="505" y="537">轴承</text></g>
<g class="hp" onclick="openPart('generator')"><title>发电机</title><rect class="pill" x="518" y="518" width="114" height="28" rx="14"/><text class="lbl" x="575" y="537">发电机</text></g>
<g class="hp" onclick="openPart('converter')"><title>变流器</title><rect class="pill" x="593" y="518" width="114" height="28" rx="14"/><text class="lbl" x="650" y="537">变流器</text></g>
<g class="hp" onclick="openPart('nacelle')"><title>机舱</title><rect class="pill" x="624" y="446" width="96" height="28" rx="14"/><text class="lbl" x="672" y="465">机舱</text></g>
<g class="hp" onclick="openPart('install')"><title>塔筒/法兰</title><rect class="pill" x="625" y="736" width="150" height="28" rx="14"/><text class="lbl" x="700" y="755">塔筒/法兰</text></g>
<g class="hp" onclick="openPart('foundation')"><title>基础</title><rect class="pill" x="252" y="994" width="96" height="28" rx="14"/><text class="lbl" x="300" y="1013">基础</text></g>
</svg>
</div>
<div class="fig-note">塔筒高100-150米 · 单机6-10MW · 混凝土/锚栓基础</div>
</div>
<div class="diagram-card">
<h3>海上风电</h3>
<div class="fig-box">
<img src="assets/sea.jpg" alt="海上风电">
<svg viewBox="0 0 1000 1250" class="ov">
<g class="hp" onclick="openPart('blade')"><title>叶片</title><rect class="pill" x="492" y="166" width="96" height="28" rx="14"/><text class="lbl" x="540" y="185">叶片</text></g>
<g class="hp" onclick="openPart('gearbox')"><title>齿轮箱</title><rect class="pill" x="283" y="518" width="114" height="28" rx="14"/><text class="lbl" x="340" y="537">齿轮箱</text></g>
<g class="hp" onclick="openPart('bearing')"><title>轴承</title><rect class="pill" x="357" y="518" width="96" height="28" rx="14"/><text class="lbl" x="405" y="537">轴承</text></g>
<g class="hp" onclick="openPart('generator')"><title>发电机</title><rect class="pill" x="418" y="518" width="114" height="28" rx="14"/><text class="lbl" x="475" y="537">发电机</text></g>
<g class="hp" onclick="openPart('converter')"><title>变流器</title><rect class="pill" x="493" y="518" width="114" height="28" rx="14"/><text class="lbl" x="550" y="537">变流器</text></g>
<g class="hp" onclick="openPart('nacelle')"><title>机舱</title><rect class="pill" x="452" y="446" width="96" height="28" rx="14"/><text class="lbl" x="500" y="465">机舱</text></g>
<g class="hp" onclick="openPart('install')"><title>塔筒</title><rect class="pill" x="102" y="676" width="96" height="28" rx="14"/><text class="lbl" x="150" y="695">塔筒</text></g>
<g class="hp" onclick="openPart('monopile')"><title>单桩/导管架</title><rect class="pill" x="471" y="1076" width="168" height="28" rx="14"/><text class="lbl" x="555" y="1095">单桩/导管架</text></g>
<g class="hp" onclick="openPart('cable')"><title>海缆</title><rect class="pill" x="602" y="1186" width="96" height="28" rx="14"/><text class="lbl" x="650" y="1205">海缆</text></g>
<g class="hp" onclick="openPart('substation')"><title>海上升压站</title><rect class="pill" x="760" y="430" width="150" height="28" rx="14"/><text class="lbl" x="835" y="449">海上升压站</text></g>
<g class="hp" onclick="openPart('installation')"><title>施工安装</title><rect class="pill" x="116" y="738" width="132" height="28" rx="14"/><text class="lbl" x="182" y="757">施工安装</text></g>
</svg>
</div>
<div class="fig-note">水深20-60米 · 单机11-18MW · 基础+海缆+升压站占投资45%+</div>
</div>
</div>
''')

S['value'] = ('五、价值量分析', '''
<h2>五、价值量分析：单GW投资构成与环节毛利分布</h2>
<h3>5.1 陆风与海风的单GW成本结构差异</h3>
<p>陆上风电单位投资约**4500-5500元/kW**（单GW约**45-55亿元**），其中整机（含塔筒）约占**40%-45%**（陆上整机不含塔筒约**1595元/kW**、含塔筒约**2120元/kW**，单GW约**16-21亿元**）、塔筒约**10%**、基础约**10%-12%**、升压站与送出线路约**15%-20%**、施工安装约**10%**、其他约**5%-10%**。</p>
<p>海上风电单位投资约**10000-13000元/kW**（单GW约**110-130亿元**），近海**9000-12500元/kW**、深远海**13000-18000元/kW**，成本结构为：整机（含塔筒）约**35%-40%**（海风含塔筒约**3280元/kW**，单GW约**33亿元**）、塔基与基础**20%-25%**、海缆**10%-15%**、施工安装**10%-15%**、升压站与送出约**10%**、其他约**5%**。海风比陆风贵**2-3倍**，但利用小时（海上约**3000-3800小时**vs陆上**2000-2400小时**）与电价（沿海资源省高）部分对冲，度电成本差距已大幅收窄。</p>
<div class="fig-chart" id="chart-invest-compare"></div>
<div class="fig-cap">图5-1 陆风与海风单GW单位投资对比（2026年口径）· 点击柱形查看成本结构</div>
<div class="fig-chart" id="chart-offshore-bom"></div>
<div class="fig-cap">图5-2 海上风电单GW投资构成（行业口径）· 点击扇区查看环节说明</div>
<div class="fig-chart" id="chart-onshore-bom"></div>
<div class="fig-cap">图5-3 陆上风电机组成本构成区间（行业口径）· 点击柱形查看部件说明</div>
<h3>5.2 各环节价值量与毛利率总览</h3>
<p class="tbl-title">表5-1 风电产业链各环节价值量与盈利水平一览</p>
<div class="tbl-wrap"><table>
<tr><th>环节</th><th>价值量（占整机/单GW）</th><th>毛利率</th><th>格局</th><th>代表公司</th></tr>
<tr><td>叶片</td><td>20%-25%（3-4亿元/GW）</td><td>约19%</td><td>双寡头</td><td>中材科技/时代新材</td></tr>
<tr><td>齿轮箱</td><td>12%-15%（2-2.4亿元/GW）</td><td>25%-30%</td><td>前三强66.7%</td><td>南高齿/采埃孚/重齿</td></tr>
<tr><td>轴承</td><td>5%-7%（0.8-1.1亿元/GW）</td><td>20%+</td><td>国产化78.4%</td><td>新强联/洛轴/瓦轴</td></tr>
<tr><td>铸锻件</td><td>5%-8%（0.8-1.3亿元/GW）</td><td>20%-25%</td><td>日月全球25-30%</td><td>日月股份/吉鑫/金雷</td></tr>
<tr><td>塔筒法兰</td><td>10%-12%（2-2.5亿元/GW）</td><td>出口35%+</td><td>CR5约55-60%</td><td>天顺/大金/泰胜</td></tr>
<tr><td>变流器</td><td>4.8%-6%（0.8-1亿元/GW）</td><td>—</td><td>第三方+自研</td><td>禾望/阳光/金风</td></tr>
<tr><td>海缆</td><td>海风投资10%-15%</td><td>26%-38%</td><td>三强垄断</td><td>东方电缆/中天/亨通</td></tr>
<tr><td>塔基（海风）</td><td>海风投资20%-25%</td><td>出口35%+</td><td>CR5约55-60%</td><td>大金/天顺/海力</td></tr>
<tr><td>整机</td><td>投资40%-45%</td><td>10%-15%</td><td>CR5约73%</td><td>金风/运达/明阳/远景/三一</td></tr>
</table></div>
<div class="conclusion">
<h4>核心判断</h4>
<ul>
<li>毛利率分布：海缆（**26%-38%**）＞齿轮箱（**25%-30%**）＞铸锻件（**20%-25%**）＞轴承（**20%+**）＞叶片（**19%**）＞整机（**10%-15%**）。</li>
<li>量价齐升集中在格局好+出海的环节：海缆（高压溢价）、出口塔基（毛利率**35%+**）、大兆瓦轴承（ASP提升）。</li>
</ul>
</div>
''')
S['economics'] = ('六、经济性与盈利拐点', '''
<h2>六、经济性与盈利拐点：从造价到IRR</h2>
<h3>6.1 LCOE与IRR测算框架</h3>
<p>度电成本（LCOE）的简化公式：LCOE=（初始投资×资本回收系数+年运维成本）/年发电量。以海上风电为例：单位投资**12000元/kW**，**25年**运营期，WACC **6.5%**，资本回收系数约**0.081**，年固定运维约**120元/kW**，利用小时**3400小时**，则LCOE=（12000×0.081+120）/3400=（972+120）/3400≈**0.32元/kWh**，与行业口径（海风度电成本约**0.3-0.4元/kWh**）一致；陆上风电LCOE已降至约**0.15-0.25元/kWh**。</p>
<p>项目全投资IRR的快速估算法：全投资IRR=（年净现金流/初始投资）的10年回收期近似，更精确用现金流折现。以浙江苍南1#海风项目为例（2026年4月公开测算）：执行保障性收购电价**0.52元/kWh**（含**0.1元**绿证溢价）、年等效利用小时**3420小时**、**25年**运营期，税后IRR为**7.2%**，高于同期10年期国债收益率约**2.8个百分点**；山东半岛南U2项目度电成本已压至**0.34元/kWh**。</p>
<p>IRR敏感性排序（影响从大到小）：电价＞利用小时＞单位投资＞运维成本。136号文后电价全面入市，电价假设成为IRR测算的最大不确定性——电价每低**0.02元/kWh**，IRR约下降**1.5个百分点**；利用小时每降**200小时**，IRR约下降**1个百分点**。不同电价假设下，同一项目IRR可在**5%-8%**之间大幅波动，这也是市场对海风项目评估存在分歧的原因。</p>
<div class="fig-chart" id="chart-irr-sens"></div>
<div class="fig-cap">图6-1 海风项目IRR对电价与利用小时的敏感性（示意模型）· 点击曲线查看该组合IRR</div>
<h3>6.2 整机盈利拐点：价格企稳与结构升级</h3>
<p>整机价格是观察板块盈利的关键。陆上风机（不含塔筒）中标均价从2021年约**3000+元/kW**一路下行至2026年8月的**1595元/kW**（含塔筒约**2120元/kW**），已处于历史低位并出现企稳迹象；海上含塔筒均价约**3280元/kW**。价格战压缩整机毛利率至**10%-15%**，但2026年出现分化：东方电气2026H1归母净利**27.13亿元**（**+42.07%**）、金风科技**18.55亿元**（**+24.67%**），两家合计占行业盈利总额约**93%**，显示价格战出清、头部盈利修复正在进行；三一重能净利**2.33亿元**（**+10.99%**），毛利率修复信号清晰。</p>
<p>整机盈利见底的三重信号——第一，价格企稳：陆上招标价已连续多月在**1600元/kW**附近波动，进一步下行空间有限（成本端钢材、玻纤价格亦在低位）；第二，结构升级：海风占比提升（海风整机价格是陆风**2倍**以上）与出口占比提升改善ASP与毛利率；第三，出清加速：中小整机厂亏损退出，头部份额持续集中。市场对整机盈利的悲观预期可能过度。海风放量、出海兑现与价格企稳下，整机龙头的盈利与估值修复空间尚未充分反映，这是2026-2027年板块的重要判断。</p>
<h3>6.3 盈利敏感性热力图：招标价×原材料成本</h3>
<p>整机商净利率对两大变量高度敏感：招标均价（收入端）与钢材/玻纤/铜/稀土等原材料成本（成本端）。以2026年基准净利率约**4%**为锚，招标价每变动**±15%**约带动净利率**±5个百分点**，原材料综合成本每变动**±20%**约反向带动净利率**±5个百分点**。热力图显示：在"招标价持平+成本上行10%"的中性偏空组合下整机净利率仅约**1.5%**，而"招标价+7.5%+成本-10%"的改善组合下净利率可达**9.1%**，这也是需要持续跟踪招标价与原材料价格的原因。</p>
<div class="fig-chart" id="chart-sens"></div>
<div class="fig-cap">图6-2 整机商净利率对招标均价与原材料成本变动的敏感性（示意模型，基准净利率4%）· 点击色块查看组合解读</div>
''')

S['stocks'] = ('七、重点公司', '''
<h2>七、重点公司：财务、估值与催化剂</h2>
<h3>7.1 整机商：格局分化，盈利修复先行者占优</h3>
<p>2026年上半年五大整机商业绩出现显著分化，是理解整机板块投资的核心切入：金风科技营收**337.39亿元**（**+18.23%**）、归母净利**18.55亿元**（**+24.67%**），动态PE约**20.8倍**，扣非净利**20.2亿元**（**+47.8%**），盈利质量稳居行业第一；东方电气（风电+火电）归母净利**27.13亿元**（**+42.07%**），与金风构成第一梯队。三一重能营收**106.6亿元**（**+24.04%**）、净利**2.33亿元**（**+10.99%**），毛利率修复信号清晰；明阳智能营收**170.36亿元**、净利**1.11亿元**（**-81.77%**），海风优势仍在但短期盈利承压；运达股份营收**138.25亿元**（**+26.9%**）、归母净利**-2.49亿元**（由盈转亏）；电气风电营收**56.54亿元**（**+112.27%**）但净利仍亏损，在手订单**23478.5MW**（**+16.66%**），订单先行、利润后至。</p>
<p class="tbl-title">表7-1 五大整机商2026H1业绩与估值一览</p>
<div class="tbl-wrap"><table>
<tr><th>公司</th><th>营收(亿元)</th><th>归母净利(亿元)</th><th>同比</th><th>总市值(亿元)</th><th>动态PE(倍)</th></tr>
<tr><td>金风科技</td><td>337.39</td><td>18.55</td><td>+24.67%</td><td>约770</td><td>约20.8</td></tr>
<tr><td>东方电气</td><td>—</td><td>27.13</td><td>+42.07%</td><td>—</td><td>—</td></tr>
<tr><td>明阳智能</td><td>170.36</td><td>1.11</td><td>-81.77%</td><td>约222</td><td>约99.9</td></tr>
<tr><td>三一重能</td><td>106.60</td><td>2.33</td><td>+10.99%</td><td>—</td><td>—</td></tr>
<tr><td>运达股份</td><td>138.25</td><td>-2.49</td><td>转亏</td><td>约73</td><td>亏损</td></tr>
<tr><td>电气风电</td><td>56.54</td><td>亏损</td><td>亏损</td><td>—</td><td>—</td></tr>
</table></div>
<div class="fig-chart" id="chart-oem-fin"></div>
<div class="fig-cap">图7-1 五大整机商2026年上半年营收与归母净利润 · 点击柱形查看公司业绩明细</div>
<h3>7.2 零部件：格局决定盈利，出海决定弹性</h3>
<p>海缆环节是风电零部件中格局最优、盈利最稳的赛道：东方电缆2025年海缆及高压电缆收入**53.63亿元**，毛利率**33.36%**（同比**+5.59pct**），总市值约**297亿元**、PE约**21.8倍**，在手订单约**193亿元**；中天科技海缆市占率约**36%-38%**，掌握**±500kV**柔性直流技术，总市值约**1201亿元**、PE约**32.3倍**；亨通光电总市值约**1613亿元**、PE约**38.5倍**。海缆环节受价格战影响小，盈利确定性高。</p>
<p>塔筒与法兰是出海弹性最大的环节：大金重工总市值约**292亿元**，2026年一致预期PE约**25倍**，欧洲海上基础市占**29.1%**居首，自有船队**24艘**（合同约**120亿元**），出口单桩毛利率**35%+**；天顺风能全球塔筒龙头，出口欧洲塔筒毛利率**35%-39%**；恒润股份为法兰龙头（市占率约**9.4%**）并延伸轴承。铸件环节日月股份国内市占约**35%**、全球约**25%-30%**，2026年预计归母净利**7-8亿元**、PE约**10-15倍**，核电第二曲线提供估值弹性；轴承环节新强联总市值约**120亿元**、PE约**14.5倍**，TRB渗透率提升+齿轮箱轴承国产化双逻辑，2026-2028年PE约**10/8/6倍**，是风电零部件中估值与成长匹配度较高的标的。</p>
<p class="tbl-title">表7-2 风电零部件重点公司估值一览（2026年9月）</p>
<div class="tbl-wrap"><table>
<tr><th>公司</th><th>环节</th><th>总市值(亿元)</th><th>PE(倍)</th><th>核心逻辑</th></tr>
<tr><td>东方电缆</td><td>海缆</td><td>约297</td><td>约21.8</td><td>在手订单193亿+高压壁垒</td></tr>
<tr><td>中天科技</td><td>海缆/光纤</td><td>约1201</td><td>约32.3</td><td>±500kV直流+多元业务</td></tr>
<tr><td>亨通光电</td><td>海缆/光纤</td><td>约1613</td><td>约38.5</td><td>海缆+算力电缆</td></tr>
<tr><td>大金重工</td><td>塔基基础</td><td>约292</td><td>约25</td><td>欧洲基础市占29.1%+自有船队</td></tr>
<tr><td>日月股份</td><td>铸件</td><td>—</td><td>约10-15</td><td>全球铸件龙头+核电曲线</td></tr>
<tr><td>新强联</td><td>轴承</td><td>约120</td><td>约14.5</td><td>TRB渗透+齿轮箱轴承国产化</td></tr>
</table></div>
<div class="fig-chart" id="chart-valuation"></div>
<div class="fig-cap">图7-2 风电重点公司估值对比（PE口径）· 点击柱形查看公司估值逻辑</div>
<h3>7.3 运营商：估值逻辑与选股</h3>
<p>风电运营商的估值逻辑是股息率、装机成长与绿电/CCER弹性：龙源电力（央企风电运营龙头）2026H1营收**146.42亿元**、归母净利**23.93亿元**，总市值约**1267亿元**、PE约**35.7倍**，海风核准与大基地开工打开长期空间；三峡能源2026H1归母净利**12.19亿元**，总市值约**1046亿元**、PE约**93.5倍**（含大量在建资产待投产）。</p>
<p>运营商选股的核心是“装机成长速度+电价结构”：新建项目全面入市后，存量项目机制电价保护与增量项目绿电溢价决定盈利预期；136号文后运营商内部回报分化加大，具备低成本获取资源能力（大基地、海风核准）、精细化运营（利用小时高于行业均值）与财务优势（低利率融资）的央企龙头占优。运营商盈利稳定，适合作为板块的基础配置，与高弹性零部件形成搭配。</p>
''')
S['mispricing'] = ('八、预期差与投资框架', '''
<h2>八、预期差与投资框架</h2>
<h3>8.1 核心预期差</h3>
<p>预期差一：市场对整机盈利的悲观外推过度，忽视海风放量、出海兑现与价格企稳下的盈利修复，整机龙头（金风等）估值有修复空间。</p>
<p>预期差二：市场低估塔基/海缆出海的持续性——欧洲产能缺口**3-5年**难解，中国企业订单排至**2027-2028年**，且自有运力构成壁垒。</p>
<p>预期差三：市场低估漂浮式的价值。2028-2030年漂浮式商业化将打开年均数十GW新增空间，当前市值尚未反映。</p>
<div class="fig-chart" id="chart-layering"></div>
<div class="fig-cap">图8-1 风电产业链环节投资价值分层（示意判断）· 点击气泡查看环节投资逻辑</div>
<h3>8.2 三维度选股框架与看好回避方向</h3>
<p>三维度选股框架：第一维度看环节格局——海缆（三强垄断）、叶片（双寡头）、轴承（国产替代加速）是格局最好的环节；第二维度看出海弹性——塔基基础（大金/天顺）、海缆（东方/中天）、整机（金风/远景）海外订单毛利率显著高于国内；第三维度看盈利拐点——整机（价格企稳+海风放量）、齿轮箱轴承（国产化）是盈利修复弹性最大的方向。</p>
<p>看好方向：海缆（东方电缆、中天科技、亨通光电）——格局最优、高压壁垒、深远海量价齐升；塔基基础出海（大金重工、天顺风能）——欧洲缺口+自有运力+毛利率**35%+**；轴承国产替代（新强联）——TRB渗透率**70%+**、齿轮箱轴承**129亿**市场；整机龙头盈利修复（金风科技、三一重能）——价格企稳、海风放量与出海兑现；叶片双寡头（中材科技、时代新材）——格局稳、碳纤维升级、海外订单。</p>
<p>回避方向：无出海能力、无海风业绩的纯陆风二三线整机/零部件厂商（价格战+份额流失双重挤压）；仅蹭风电概念而无订单验证的公司；高估值且盈利持续亏损的整机商（除非海风业绩明确兑现）；过度依赖国内补贴退坡前抢装逻辑的环节。</p>
<p class="tbl-title">表8-1 投资框架速查表</p>
<div class="tbl-wrap"><table>
<tr><th>维度</th><th>看好</th><th>逻辑</th><th>跟踪指标</th></tr>
<tr><td>海缆</td><td>东方电缆/中天/亨通</td><td>高压垄断+深远海量价</td><td>海缆中标订单</td></tr>
<tr><td>塔基出海</td><td>大金重工/天顺风能</td><td>欧洲缺口+自有运力</td><td>欧洲单桩订单/船队</td></tr>
<tr><td>轴承</td><td>新强联</td><td>TRB渗透+国产替代</td><td>TRB渗透率/齿轮箱轴承验证</td></tr>
<tr><td>整机</td><td>金风/三一</td><td>盈利拐点+海风放量</td><td>中标价格/海风吊装</td></tr>
<tr><td>叶片</td><td>中材科技/时代新材</td><td>双寡头+碳纤维+海外</td><td>叶片出货/碳纤维价格</td></tr>
</table></div>
<div class="conclusion">
<h4>核心判断</h4>
<ul>
<li>核心配置：东方电缆、金风科技——格局优、盈利稳、订单确定。</li>
<li>弹性配置：大金重工、新强联、三一重能——出海与国产替代弹性。</li>
<li>弹性配置：明阳智能、漂浮式链——海风放量与深远海开发。</li>
<li>基础配置：龙源电力——公用事业属性、股息稳定。</li>
</ul>
</div>
''')

S['risk'] = ('九、风险提示', '''
<h2>九、风险提示与跟踪指标</h2>
<h3>9.1 核心风险</h3>
<p>第一，电价下行风险：136号文后新能源全面入市，市场化电价下行直接压制运营商IRR与项目收益确定性；机制电价竞价结果低于预期将影响装机节奏。第二，原材料价格风险：钢材、玻纤、稀土、铜等原材料价格波动向产业链传导，成本上行挤压零部件毛利率。</p>
<p>第三，海风进度不及预期风险：船机资源是海风装机的真正瓶颈（中国WTIV在册**42艘**，需新增**15-20艘**），施工窗口受季风期限制，吊装进度低于预期将推迟业绩兑现。第四，海外贸易壁垒风险：中国风电产品出海面临关税、反倾销、认证与本地化要求等潜在壁垒。第五，政策变化风险：补贴退坡、并网政策、机制电价细则调整均可能影响行业盈利模型。</p>
<h3>9.2 跟踪指标清单</h3>
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
</table></div>
<div class="conclusion">
<h4>核心判断</h4>
<ul>
<li>核心验证信号：整机价格企稳（**1600元/kW**附近不再下行）、海风月度吊装放量（船机利用率提升）、零部件企业毛利率环比改善。</li>
<li>行业景气持续性的锚：招标量×1.5-2年周期=未来装机，2026年1-8月央国企中标**105.98GW**为2027-2028年装机提供确定性。</li>
</ul>
</div>
''')

# ============ 组装 ============
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif;background:#0f1117;color:#d1d5db;line-height:1.75}
.container{max-width:1280px;margin:0 auto;padding:20px}
.nav{position:sticky;top:0;background:rgba(15,17,23,0.96);backdrop-filter:blur(10px);padding:14px 0;border-bottom:1px solid #2a2d3a;z-index:100;display:flex;flex-wrap:wrap;gap:6px;justify-content:center}
.nav a{color:#9aa1b2;text-decoration:none;padding:6px 12px;border-radius:6px;font-size:13px;transition:all .2s}
.nav a:hover,.nav a.active{color:#fff;background:#2563eb}
.section{margin:36px 0;padding:30px;background:#181b24;border-radius:12px;border:1px solid #252836}
h1{font-size:34px;margin-bottom:8px;color:#fff}
h2{font-size:23px;margin-bottom:18px;color:#fff;border-left:4px solid #3b82f6;padding-left:12px}
h3{font-size:17px;margin:22px 0 12px;color:#fff}
p{font-size:14px;color:#d1d5db;margin:10px 0;text-align:justify}
p.lead{font-size:15px;color:#d1d5db;margin:14px 0;border-left:3px solid #3b82f6;padding-left:12px}
mark{background:rgba(239,68,68,0.18);color:#fca5a5;padding:1px 4px;border-radius:3px;border-bottom:2px solid #ef4444;font-weight:600}
.conclusion{margin:18px 0;padding:16px 20px;background:linear-gradient(90deg,rgba(59,130,246,0.08),rgba(59,130,246,0.02));border-left:3px solid #3b82f6;border-radius:8px}
.conclusion h4{color:#fff;font-size:14px;margin-bottom:8px}
.conclusion ul{list-style:none}
.conclusion li{font-size:13.5px;color:#d1d5db;margin:6px 0;padding-left:14px;position:relative}
.conclusion li:before{content:'';position:absolute;left:0;top:8px;width:6px;height:6px;border-radius:50%;background:#3b82f6}
.grid{display:grid;gap:14px;margin:16px 0}
.grid-4{grid-template-columns:repeat(4,1fr)}
.grid-3{grid-template-columns:repeat(3,1fr)}
.card{background:#1e2230;border:1px solid #252836;border-radius:10px;padding:16px}
.card h3{font-size:15px;margin-bottom:8px;color:#fff}
.card p{font-size:13px;color:#d1d5db;margin:0}
.metric{text-align:center;padding:20px 14px}
.metric-value{font-size:26px;font-weight:700;color:#60a5fa;margin-bottom:6px}
.metric-label{font-size:12px;color:#9aa1b2}
.card-highlight{border-color:rgba(34,197,94,0.4)}
.card-highlight h3{color:#22c55e}
.card-warning{border-color:rgba(245,158,11,0.4)}
.card-warning h3{color:#f59e0b}
.card-danger{border-color:rgba(239,68,68,0.4)}
.card-danger h3{color:#ef4444}
.fig-chart{height:380px;margin:16px 0 6px}
.diagram-wrap{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:16px 0}
.diagram-card{background:#1a1e2a;border:1px solid #252836;border-radius:10px;padding:14px}
.diagram-card h3{font-size:15px;margin:0 0 6px;color:#fff}
.fig-box{position:relative;border-radius:8px;overflow:hidden;background:#0b0e16}
.fig-box img{width:100%;display:block}
.fig-box .ov{position:absolute;inset:0;width:100%;height:100%}
.hp{cursor:pointer}
.hp .pill{fill:#2563eb;fill-opacity:.88;stroke:none;transition:fill .15s,fill-opacity .15s}
.hp:hover .pill{fill:#1e40af;fill-opacity:1}
.hp .lbl{fill:#fff;font-size:18px;font-weight:600;pointer-events:none;text-anchor:middle}
.fig-note{font-size:11px;color:#9aa1b2;text-align:center;margin-top:8px}
.sub-list{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}
.sub-list button{background:#252a3a;border:1px solid #3b82f6;color:#e4e6eb;padding:8px 16px;border-radius:8px;cursor:pointer;font-size:13px;transition:all .15s}
.sub-list button:hover{background:#2563eb;color:#fff}
.part-img{width:100%;border-radius:8px;margin:4px 0 10px;display:block}
.cmp-title{font-size:13px;color:#fff;font-weight:600;margin:12px 0 4px}
.fig-cap{font-size:12px;color:#9aa1b2;text-align:center;margin:0 0 14px}
.tbl-title{font-size:13px;color:#d1d5db;font-weight:600;margin:16px 0 6px}
.tbl-wrap{overflow-x:auto;margin:10px 0}
table{width:100%;border-collapse:collapse;font-size:13px}
th{background:#252836;padding:9px 12px;text-align:left;color:#fff;font-weight:600;border-bottom:2px solid #3b82f6;white-space:nowrap}
td{padding:9px 12px;border-bottom:1px solid #252836;color:#d1d5db}
tr:hover{background:rgba(59,130,246,0.05)}
.chain-layer{margin:14px 0;border:1px solid #252836;border-radius:10px;background:#1a1e2a;overflow:hidden}
.chain-layer-title{padding:10px 16px;background:#20263a;color:#fff;font-size:13.5px;font-weight:600;border-bottom:1px solid #252836}
.chain-items{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:12px 16px}
.chain-item{font-size:12.5px;color:#d1d5db;background:#252a3a;border:1px solid #2a2f42;border-radius:6px;padding:5px 10px}
.chain-item-hot{border-color:rgba(239,68,68,0.5);color:#fca5a5;background:rgba(239,68,68,0.08)}
.toolbar{position:sticky;top:52px;z-index:90;display:flex;justify-content:center;gap:10px;padding:10px 0;background:rgba(15,17,23,0.9);backdrop-filter:blur(8px);border-bottom:1px solid #252836}
.toolbar button{background:#1e2230;border:1px solid #2a2d3a;color:#9aa1b2;padding:6px 18px;border-radius:6px;cursor:pointer;font-size:13px;transition:all .2s}
.toolbar button:hover,.toolbar button.active{background:#2563eb;color:#fff;border-color:#2563eb}
body.mode-red p:not(.has-red),body.mode-red .lead{display:none}
body.mode-red .fig-chart,body.mode-red .fig-cap,body.mode-red .tbl-wrap,body.mode-red .tbl-title{display:none}
body.mode-red h3{display:none}
body.mode-red .chain-layer{display:none}
.modal{position:fixed;inset:0;background:rgba(0,0,0,0.65);z-index:300;display:none;align-items:center;justify-content:center;padding:20px}
.modal.show{display:flex}
.modal-box{background:#1e2230;border:1px solid #2a2d3a;border-radius:12px;max-width:720px;width:100%;max-height:82vh;overflow:auto;padding:24px;position:relative}
.modal-close{position:absolute;top:12px;right:14px;background:none;border:none;color:#9aa1b2;font-size:22px;cursor:pointer;line-height:1}
.modal-box h3{color:#fff;font-size:18px;margin-bottom:4px}
.modal-sub{color:#9aa1b2;font-size:12px;margin-bottom:14px}
.modal-box table{font-size:12.5px}
.footer{text-align:center;padding:36px 20px;color:#6b7280;font-size:12px;border-top:1px solid #252836;margin-top:50px}
@media(max-width:900px){.grid-4{grid-template-columns:repeat(2,1fr)}.grid-3{grid-template-columns:1fr}.diagram-wrap{grid-template-columns:1fr}}
@media(max-width:768px){.chain-items{grid-template-columns:repeat(2,1fr)}.section{padding:20px 14px}.nav a{font-size:12px;padding:10px 10px;min-height:44px;display:inline-flex;align-items:center}h2{font-size:19px}h3{font-size:15px}p{font-size:14px}.toolbar button{min-height:44px}.fig-chart{height:320px}}
"""
# ---- 图表弹窗数据 ----
D_ANNUAL = {
'2025A': ('中国风电新增装机结构（2025实际）', '合计约100GW · 全球首个年新增突破100GW市场', '<p>2025年中国新增装机约**100GW**：陆上**93.4GW**、海上**6.6GW**。中国海风新增连续第八年全球第一；沙戈荒大基地与分散式贡献主要增量。</p>'),
'2026E': ('中国风电新增装机结构（2026预计）', '合计约115GW · 海风同比+30%', '<p>2026年中国新增装机约**115GW**：陆上**105GW**、海上**10GW**。机制电价竞价落地约**7000万千瓦**装机底盘，海风进入放量爬坡期。</p>'),
'十五年均': ('中国风电新增装机结构（十五五年均）', '合计约120GW · 风能北京宣言2.0目标', '<p>“十五五”期间中国风电年新增不低于**1.2亿千瓦**：陆上约**105GW**、海上**15GW**（不低于1500万千瓦）。2030年累计装机**13亿千瓦**、海风累计**1亿千瓦以上**。</p>')
}
D_GLOBAL = {
'2025A': ('全球海上风电新增并网（2025实际）', 'GWEC口径', '<p>全球海风新增并网**9.3GW**（同比+16%），为历史第三高年度；累计装机**92.5GW**。中国以6.6GW居首，英国、德国、荷兰居欧洲前三。</p>'),
'2026E': ('全球海上风电新增并网（2026预计）', 'GWEC口径', '<p>全球海风新增约**13GW**。欧洲北海项目集中建设（英国5GW+、荷兰3GW+），中国继续放量，亚太（越南、菲律宾）启动。</p>'),
'2028E': ('全球海上风电新增并网（2028预计）', 'GWEC口径', '<p>全球海风新增约**22GW**。欧洲大型海上风电集群（1GW+单体项目）密集并网，中国“十五五”海风年增爬坡至15GW附近。</p>'),
'2030E': ('全球海上风电新增并网（2030预计）', 'GWEC口径', '<p>全球海风新增约**33GW**，海风占风电新增比例升至**16%**。漂浮式开始商业化，亚太与美洲贡献增量。</p>')
}
D_INVEST = {
'陆上风电': ('陆上风电单GW单位投资', '约50亿元/GW', '<p>整机（含塔筒）占**40%-45%**、塔筒**10%**、基础**10%-12%**、升压站与送出**15%-20%**、施工**10%**。度电成本约**0.15-0.25元/kWh**，全面平价。</p>'),
'近海风电': ('近海风电单GW单位投资', '约120亿元/GW', '<p>整机（含塔筒）占**35%-40%**、塔基与基础**20%-25%**、海缆**10%-15%**、施工**10%-15%**。近海利用小时约**3000-3500h**，度电成本约**0.3-0.4元/kWh**。</p>'),
'深远海风电': ('深远海风电单GW单位投资', '约155亿元/GW', '<p>水深50米以上，单桩升级为导管架/漂浮式基础，海缆长度与电压等级提升。单GW投资**130-180亿元**，需漂浮式商业化后进一步降本。</p>')
}
D_BOM_OFFSHORE = {
'整机（含塔筒）': ('海上风电整机（含塔筒）', '占单GW投资38% · 约33亿元/GW', '<p>海风含塔筒中标均价约**3280元/kW**。单机容量**11-18MW**为主力，大型化摊薄单位造价；代表：金风/明阳/远景/运达/三一。</p>'),
'塔基与基础': ('塔基与基础（单桩/导管架）', '占单GW投资23% · 约24-36亿元/GW', '<p>大金重工（欧洲**29.1%**）、天顺风能、海力风电、泰胜风能。万吨级单桩需深水码头与大型门式起重机，出口毛利率**35%+**。</p>'),
'施工安装': ('海上施工安装', '占单GW投资12%', '<p>中国WTIV在册**42艘**，需新增**15-20艘**大吨位船。船机资源是海风装机的真正瓶颈，跟踪吊装进度比招标量更能反映真实放量。</p>'),
'海缆': ('海缆（阵列+送出）', '占单GW投资12% · 约12-18亿元/GW', '<p>中天**36%-38%**、东方电缆**25%**、亨通**18%**三强垄断。电压等级从66kV阵列向330kV送出、±525kV直流跃迁，单GW价值量持续提升。</p>'),
'叶片': ('海上风电叶片', '占单GW投资8%', '<p>中材科技（国内**28.9%**）+时代新材（**24%**）双寡头。海上叶片长度**110-130米**，碳纤维主梁渗透率提升。</p>'),
'其他': ('其他（升压站/变流/勘测等）', '占单GW投资7%', '<p>海上升压站、动态海缆、勘测设计等，随离岸距离增加占比上升。</p>')
}
D_BOM_ONSHORE = {
'叶片': ('叶片占整机成本', '22.5% · 价值量最大的单一零部件', '<p>中材科技（全球第一）+时代新材双寡头，毛利率约**18.9%**。碳纤维主梁渗透+海外订单是主要预期差。</p>'),
'齿轮箱': ('齿轮箱占整机成本', '13.5% · 单GW约2-2.4亿元', '<p>南高齿**23.4%**+采埃孚**22.7%**+重齿**20.6%**（前三强**66.7%**）。毛利率**25%-30%**，半直驱渗透+海风大兆瓦溢价。</p>'),
'塔筒': ('塔筒占整机成本', '11.0% · 单GW约2-2.5亿元', '<p>天顺**21.3%**、大金**17.3%**、泰胜**13.8%**。出口欧洲毛利率**35%+**，欧洲产能缺口3-5年难解。</p>'),
'发电机': ('发电机占整机成本', '9.0%', '<p>大型化下发电机单机功率提升，直驱/半直驱路线影响其价值量结构。</p>'),
'轴承': ('轴承占整机成本', '6.0% · 单GW约0.8-1.1亿元', '<p>国产化率整体**78.4%**（偏航变桨**91.3%**、主轴**70.5%**）。新强联TRB渗透率**70%+**，齿轮箱轴承国产化是**129亿**市场。</p>'),
'变流器': ('变流器占整机成本', '5.4% · 单GW约0.8-1亿元', '<p>禾望电气、阳光电源为第三方龙头，构网型变流器成为沙戈荒基地标配。</p>'),
'其他': ('其他（机舱罩/线缆/控制系统等）', '12.5%', '<p>含机舱罩、线缆、控制系统、辅材等。</p>')
}
D_IRR = {'电价 0.30元/kWh': '电价0.30元/kWh（低电价情景）', '电价 0.35元/kWh': '电价0.35元/kWh（基准偏悲观）', '电价 0.40元/kWh': '电价0.40元/kWh（基准情景）', '电价 0.45元/kWh': '电价0.45元/kWh（含绿电溢价）'}
D_OEM = {
'金风科技': ('金风科技 · 整机龙头', '营收337.39亿元 / 归母净利18.55亿元', '<p>营收**337.39亿元**（+18.23%）、归母净利**18.55亿元**（+24.67%）、扣非**20.2亿元**（+47.8%）。动态PE约**20.8倍**，盈利质量行业第一，海风放量、出海兑现与价格企稳。</p>'),
'明阳智能': ('明阳智能 · 海上整机龙头', '营收170.36亿元 / 归母净利1.11亿元', '<p>营收**170.36亿元**、净利**1.11亿元**（-81.77%）。海风优势仍在但短期盈利承压，海风放量后盈利拐点期权标的。</p>'),
'三一重能': ('三一重能 · 盈利修复标的', '营收106.6亿元 / 归母净利2.33亿元', '<p>营收**106.6亿元**（+24.04%）、净利**2.33亿元**（+10.99%）。毛利率修复与份额提升兼具，估值处于低位。</p>'),
'运达股份': ('运达股份 · 份额提升但亏损', '营收138.25亿元 / 归母净利-2.49亿元', '<p>营收**138.25亿元**（+26.9%）但归母净利**-2.49亿元**（由盈转亏）。价格战下盈利承压，需跟踪价格企稳后的盈利修复。</p>'),
'电气风电': ('电气风电 · 订单先行', '营收56.54亿元 / 净利亏损', '<p>营收**56.54亿元**（+112.27%）、在手订单**23478.5MW**（+16.66%）。订单先行、利润后至，海风放量是核心催化。</p>')
}
D_VAL = {
'金风科技': ('金风科技', '动态PE 20.8倍', '<p>盈利确定性最强的整机龙头：扣非+47.8%、海风+出海结构升级，盈利与估值双修复空间最大。</p>'),
'东方电缆': ('东方电缆', '动态PE 21.8倍', '<p>海缆毛利率**33.36%**、在手订单**193亿元**。高压+深远的确定性溢价标的，估值与成长匹配度高。</p>'),
'大金重工': ('大金重工', '动态PE 25倍（2026E）', '<p>欧洲海上基础市占**29.1%**居首、自有船队**24艘**（合同**120亿**）、出口单桩毛利率**35%+**，出海弹性最大。</p>'),
'新强联': ('新强联', '动态PE 14.5倍', '<p>TRB渗透率**70%+**+齿轮箱轴承国产化（**129亿**市场）双逻辑，2026-2028年PE约**10/8/6倍**。</p>'),
'中天科技': ('中天科技', '动态PE 32.3倍', '<p>海缆市占**36%-38%**、掌握**±500kV**柔性直流技术，光通信+海洋双主业。</p>'),
'亨通光电': ('亨通光电', '动态PE 38.5倍', '<p>海缆市占**18%**+算力电缆第二曲线，估值含多业务溢价。</p>'),
'龙源电力': ('龙源电力', '动态PE 35.7倍', '<p>央企风电运营龙头：营收**146.42亿元**、净利**23.93亿元**，海风核准与大基地开工打开成长空间，盈利稳定。</p>'),
'三峡能源': ('三峡能源', '动态PE 93.5倍', '<p>净利**12.19亿元**（含大量在建资产待投产）。装机成长最快，投产兑现后估值有望消化。</p>')
}
D_LAYER = {
'海缆': ('海缆', '景气确定性85 · 盈利弹性72', '<p>三强垄断+高压壁垒+深远海量价齐升，是风电确定性溢价最高的环节。</p>'),
'塔基基础': ('塔基基础（出海）', '景气确定性80 · 盈利弹性76', '<p>欧洲产能缺口与自有运力构成壁垒，出口毛利率**35%+**，订单排至2027-2028年。</p>'),
'轴承': ('轴承（国产替代）', '景气确定性72 · 盈利弹性68', '<p>TRB渗透率**70%+**+齿轮箱轴承国产化，129亿市场是最大替代空间。</p>'),
'整机': ('整机（盈利拐点）', '景气确定性68 · 盈利弹性62', '<p>价格企稳、海风放量与出海兑现下，盈利修复弹性最大，但格局波动较大。</p>'),
'叶片': ('叶片（双寡头）', '景气确定性75 · 盈利弹性42', '<p>中材+时代新材双寡头，格局稳但盈利弹性偏弱，看碳纤维与海外。</p>'),
'齿轮箱': ('齿轮箱（半直驱）', '景气确定性72 · 盈利弹性52', '<p>前三强**66.7%**集中，半直驱渗透+海风大兆瓦溢价。</p>'),
'铸锻件': ('铸锻件（大型化）', '景气确定性66 · 盈利弹性46', '<p>日月股份全球**25-30%**，海风大型化提升单GW价值量，核电第二曲线。</p>'),
'变流器': ('变流器（构网型）', '景气确定性62 · 盈利弹性42', '<p>构网型成为沙戈荒标配，IGBT国产化与SiC渗透带来成本下行。</p>'),
'运营商': ('运营商（类公用）', '景气确定性70 · 盈利弹性32', '<p>股息率、装机成长与绿电/CCER弹性，盈利稳定。</p>'),
'漂浮式': ('漂浮式（远期期权）', '景气确定性42 · 盈利弹性58', '<p>2028-2030年商业化打开深远海**70%**空间，当前尚未定价。</p>')
}

D_PARTS = {
'blade': ('叶片','占整机成本20%-25% · 陆上单GW约3-4亿元','<img src="assets/parts/blade.jpg" class="part-img"><p>占整机成本**20%-25%**（陆上单GW约**3-4亿元**）。中材科技（全球第一、国内**28.9%**）+时代新材（约**24%**）双寡头，毛利率约**18.9%**。大兆瓦化后海上叶片长度增至**110-130米**，碳纤维主梁渗透率提升，海外订单（欧洲订单增**30%**）打开第二曲线。</p><p class="cmp-title">主要参与公司产品对比</p><div class="tbl-wrap"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>中材科技</td><td>百米级玻纤/碳纤维主梁叶片</td><td>全球第一、国内28.9%</td></tr><tr><td>时代新材</td><td>海上大兆瓦叶片</td><td>国内约24%</td></tr></table></div>'),
'gearbox': ('齿轮箱','占整机成本12%-15% · 单GW约2-2.4亿元','<img src="assets/parts/gearbox.jpg" class="part-img"><p>南高齿**23.4%**+采埃孚**22.7%**+重齿**20.6%**，前三强集中度**66.7%**，毛利率**25%-30%**。半直驱渗透+大兆瓦海风齿轮箱溢价+海外主机厂采购放量是主要预期差。</p><p class="cmp-title">主要参与公司产品对比</p><div class="tbl-wrap"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>南高齿</td><td>双馈/半直驱主齿轮箱</td><td>23.4%份额</td></tr><tr><td>采埃孚</td><td>风电主齿轮箱</td><td>22.7%份额</td></tr><tr><td>重齿</td><td>大型风电齿轮箱</td><td>20.6%份额</td></tr></table></div>'),
'generator': ('发电机','占整机成本约9%','<img src="assets/parts/generator.jpg" class="part-img"><p>大型化下单机功率持续提升（海上**11-18MW**），直驱（永磁同步）与半直驱（中速永磁）路线占比上升。金风、明阳以自研为主，中车株洲电机、东电电机等供应部分整机商。</p><p class="cmp-title">主要参与公司产品对比</p><div class="tbl-wrap"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>中车株洲电机</td><td>永磁直驱/半直驱发电机</td><td>第三方龙头</td></tr><tr><td>东方电机</td><td>大型风力发电机</td><td>配套整机商</td></tr><tr><td>金风/明阳</td><td>自研发电机</td><td>垂直一体化</td></tr></table></div>'),
'bearing': ('轴承','占整机成本5%-7% · 单GW约0.8-1.1亿元','<img src="assets/parts/bearing.jpg" class="part-img"><p>国产化率整体**78.4%**（偏航变桨**91.3%**、主轴**70.5%**）。新强联TRB（双列圆锥滚子）渗透率**70%+**，洛轴、瓦轴跟进；齿轮箱轴承国产化（**129亿**市场）是最大替代空间。</p><p class="cmp-title">主要参与公司产品对比</p><div class="tbl-wrap"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>新强联</td><td>TRB主轴轴承</td><td>渗透率70%+</td></tr><tr><td>洛轴</td><td>偏航变桨/主轴轴承</td><td>国产化主力</td></tr><tr><td>瓦轴</td><td>大型风电轴承</td><td>国产化跟随</td></tr></table></div>'),
'converter': ('变流器','占整机成本4.8%-6% · 单GW约0.8-1亿元','<img src="assets/parts/converter.jpg" class="part-img"><p>禾望电气、阳光电源为第三方龙头，金风/远景/明阳自研比例上升。构网型变流器成为沙戈荒大基地与新型电力系统标配；IGBT国产化与SiC渗透带来成本下行。</p><p class="cmp-title">主要参与公司产品对比</p><div class="tbl-wrap"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>禾望电气</td><td>风电变流器</td><td>第三方龙头</td></tr><tr><td>阳光电源</td><td>风电变流器</td><td>头部供应商</td></tr><tr><td>金风/远景</td><td>自研变流器</td><td>垂直一体化</td></tr></table></div>'),
'nacelle': ('机舱总成','机舱罩+主轴+齿轮箱+发电机等核心总成','<img src="assets/parts/nacelle.jpg" class="part-img"><p>机舱内集成主轴、齿轮箱、发电机、变流器、控制系统等核心部件，是整机技术含量最高的总成。机舱内细色块对应**齿轮箱/轴承/发电机/变流器**，可分别查看。</p><p class="cmp-title">主要参与公司产品对比</p><div class="tbl-wrap"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>金风科技</td><td>直驱/半直驱机舱总成</td><td>整机龙头</td></tr><tr><td>明阳智能</td><td>海上机舱总成</td><td>海风领先</td></tr><tr><td>远景能源</td><td>智能机舱总成</td><td>全球出货前三</td></tr></table></div>'),
'install': ('装机与基础（细分选择）','点击下方环节查看具体分析','<div class="sub-list"><button onclick="showPart(\'tower\')">塔筒</button><button onclick="showPart(\'flange\')">法兰</button><button onclick="showPart(\'monopile\')">单桩</button><button onclick="showPart(\'jacket\')">导管架</button><button onclick="showPart(\'foundation\')">陆上基础</button></div>'),
'tower': ('塔筒','占整机成本10%-12% · 单GW约2-2.5亿元；海风塔筒+基础占20%-30%','<img src="assets/parts/tower.jpg" class="part-img"><p>天顺**21.3%**、大金**17.3%**、泰胜**13.8%**（CR5约**55%-60%**）。大兆瓦化提升单机塔筒重量与价值量；出口欧洲塔筒毛利率**35%-39%**。</p><p class="cmp-title">主要参与公司产品对比</p><div class="tbl-wrap"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>天顺风能</td><td>陆海塔筒</td><td>21.3%份额</td></tr><tr><td>大金重工</td><td>塔筒+基础</td><td>17.3%份额</td></tr><tr><td>泰胜风能</td><td>陆海塔筒</td><td>13.8%份额</td></tr></table></div>'),
'flange': ('法兰','塔筒节间/塔筒-基础连接锻件 · 恒润股份市占约9.4%','<img src="assets/parts/flange.jpg" class="part-img"><p>法兰是塔筒节间与塔筒-基础连接的关键锻件，恒润股份为龙头（市占率约**9.4%**）并延伸轴承业务。出海与大型化提升单GW价值量。</p><p class="cmp-title">主要参与公司产品对比</p><div class="tbl-wrap"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>恒润股份</td><td>风电法兰+轴承</td><td>市占约9.4%</td></tr><tr><td>大金重工</td><td>塔筒+法兰集成</td><td>欧洲基础29.1%</td></tr><tr><td>天顺风能</td><td>塔筒+法兰集成</td><td>全球塔筒龙头</td></tr></table></div>'),
'monopile': ('单桩基础（海上）','占海风单GW投资20%-25% · 出海第一赛道','<img src="assets/parts/monopile.jpg" class="part-img"><p>大金重工欧洲海上基础市占**29.1%**居首、自有船队**24艘**（合同约**120亿**）、出口单桩毛利率**35%+**；天顺、海力、泰胜跟随。万吨级单桩需深水码头+大型门式起重机，出口资质稀缺。</p><p class="cmp-title">主要参与公司产品对比</p><div class="tbl-wrap"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>大金重工</td><td>海上单桩</td><td>欧洲29.1%居首</td></tr><tr><td>天顺风能</td><td>单桩/导管架</td><td>出口主力</td></tr><tr><td>海力风电</td><td>海上基础</td><td>跟随放量</td></tr></table></div>'),
'jacket': ('导管架基础（海上）','适用于水深40-60米 · 价值量高于单桩','<img src="assets/parts/jacket.jpg" class="part-img"><p>随水深增加，导管架/吸力筒基础占比提升。欧洲北海多采用导管架，中国企业导管架产能与出口订单同步放量，是迈向深远海的重要基础形式。</p><p class="cmp-title">主要参与公司产品对比</p><div class="tbl-wrap"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>海力风电</td><td>导管架/吸力筒</td><td>海上基础专精</td></tr><tr><td>泰胜风能</td><td>导管架+塔筒</td><td>多品类布局</td></tr><tr><td>大金重工</td><td>导管架出口</td><td>欧洲订单</td></tr></table></div>'),
'foundation': ('陆上基础','混凝土扩展基础/锚栓 · 占陆上投资10%-12%','<img src="assets/parts/foundation.jpg" class="part-img"><p>陆上风机基础以混凝土扩展基础与岩石锚杆基础为主，占陆上单GW投资约**10%-12%**。沙戈荒地区采用预应力锚栓基础，随大兆瓦机组载荷提升，基础造价上行。</p><p class="cmp-title">主要参与公司产品对比</p><div class="tbl-wrap"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>中国能建</td><td>风电基础EPC</td><td>央企施工</td></tr><tr><td>中国电建</td><td>风电基础施工</td><td>央企施工</td></tr><tr><td>中交集团</td><td>基础+海工施工</td><td>一体化</td></tr></table></div>'),
'cable': ('海缆（阵列+送出）','占海风单GW投资10%-15% · 约12-18亿元/GW','<img src="assets/parts/cable.jpg" class="part-img"><p>中天**36%-38%**、东方电缆**25%**、亨通**18%**三强垄断，三家具备**500kV**交付能力。东方电缆海缆毛利率**33.36%**、在手订单**193亿**。电压等级从66kV阵列→330kV送出→±525kV直流跃迁，单GW价值量持续提升。</p><p class="cmp-title">主要参与公司产品对比</p><div class="tbl-wrap"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>中天科技</td><td>±500kV柔性直流海缆</td><td>市占36%-38%</td></tr><tr><td>东方电缆</td><td>330kV/500kV海缆</td><td>毛利率33.36%、订单193亿</td></tr><tr><td>亨通光电</td><td>高压海缆</td><td>市占约18%</td></tr></table></div>'),
'substation': ('海上升压站','占海风投资约4%-5% · 随离岸距离提升价值量','<img src="assets/parts/substation.jpg" class="part-img"><p>海上升压站将阵列电压升压后经送出缆上网，随离岸距离与场址容量提升，500kV/±525kV送出成为主流，升压站价值量同步提升。代表：特变电工、中天科技（海缆+电气设备协同）。</p><p class="cmp-title">主要参与公司产品对比</p><div class="tbl-wrap"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>特变电工</td><td>海上升压站主变压器</td><td>变压器龙头</td></tr><tr><td>中天科技</td><td>海缆+电气设备协同</td><td>海缆龙头</td></tr><tr><td>正泰电气</td><td>升压站成套设备</td><td>头部供应商</td></tr></table></div>'),
'installation': ('施工安装（船机）','占海风投资10%-15% · 船机是瓶颈','<img src="assets/parts/installation.jpg" class="part-img"><p>中国WTIV在册**42艘**，需新增**15-20艘**大吨位船。船机资源是海风装机的真正瓶颈，跟踪吊装进度比招标量更能反映真实放量。受益：广州打捞局、中交系统、龙源振华。</p><p class="cmp-title">主要参与公司产品对比</p><div class="tbl-wrap"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>广州打捞局</td><td>自升式风电安装船</td><td>WTIV运营</td></tr><tr><td>中交系统</td><td>海上风电施工总包</td><td>船队+施工</td></tr><tr><td>龙源振华</td><td>海上风电安装</td><td>专业安装</td></tr></table></div>')
}
FUNC_JS = r"""
function toggleMode(){var b=document.getElementById('btn-red');document.body.classList.toggle('mode-red');b.classList.toggle('active');b.textContent=document.body.classList.contains('mode-red')?'显示全部内容':'只看关键数据';}
function scrollTop0(){window.scrollTo({top:0,behavior:'smooth'});}
window.addEventListener('scroll',function(){var y=window.scrollY+120;var cur='';document.querySelectorAll('.section').forEach(function(s){if(s.offsetTop<=y)cur=s.id;});document.querySelectorAll('.nav a').forEach(function(a){a.classList.toggle('active',a.getAttribute('href')==='#'+cur);});},{passive:true});
function openModal(t,s,b){document.getElementById('modalTitle').textContent=t;document.getElementById('modalSub').textContent=s;document.getElementById('modalBody').innerHTML=md(b);document.getElementById('chartModal').classList.add('show');}
function md(s){return s.split('**').map(function(x,i){return i%2?('<mark>'+x+'</mark>'):x;}).join('');}
function openPart(k){var v=window['D_PARTS'][k];if(v)openModal(v[0],v[1],v[2]);}
function showPart(k){openPart(k);}
function closeModal(){document.getElementById('chartModal').classList.remove('show');}
document.addEventListener('click',function(e){if(e.target.id==='chartModal')closeModal();});
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeModal();});
"""

CHART_JS = r"""
var ED='https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js';
document.write('<script src="'+ED+'"><\/script>');
function initCharts(){ if(typeof echarts==='undefined'){ setTimeout(initCharts,200); return; }
var D={};
D['annual']={name:'2025A',off:9.3,on:93.4};
"""

CHART_JS2 = r"""
function gd(id){ return document.getElementById(id); }
var c1=echarts.init(gd('chart-annual'));
c1.setOption({
tooltip:{trigger:'axis',axisPointer:{type:'shadow'},backgroundColor:'#252836',borderColor:'#3b82f6',textStyle:{color:'#e4e6eb'}},
legend:{data:['陆上风电','海上风电'],textStyle:{color:'#9aa1b2'},top:0},
grid:{left:'8%',right:'4%',top:'18%',bottom:'8%'},
xAxis:{type:'category',data:['2025A','2026E','十五年均'],axisLabel:{color:'#9aa1b2'},axisLine:{lineStyle:{color:'#2a2d3a'}}},
yAxis:{type:'value',name:'GW',nameTextStyle:{color:'#9aa1b2'},axisLabel:{color:'#9aa1b2'},splitLine:{lineStyle:{color:'#252836'}}},
series:[
{name:'陆上风电',type:'bar',stack:'a',barWidth:56,data:[93.4,105,105],itemStyle:{color:new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'#3b82f6'},{offset:1,color:'#1e40af'}])},label:{show:true,position:'inside',color:'#fff',fontSize:11,formatter:function(p){return p.value;}}},
{name:'海上风电',type:'bar',stack:'a',barWidth:56,data:[6.6,10,15],itemStyle:{color:new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'#a78bfa'},{offset:1,color:'#6d28d9'}])},label:{show:true,position:'top',color:'#e4e6eb',fontSize:11}}
]});
c1.on('click',function(p){var cats=['2025A','2026E','十五年均'];var k=cats[p.dataIndex];var v=window['D_ANNUAL'][k];if(v)openModal(v[0],v[1],v[2]);});

var c2=echarts.init(gd('chart-global-offshore'));
c2.setOption({
tooltip:{trigger:'axis',axisPointer:{type:'shadow'},backgroundColor:'#252836',borderColor:'#3b82f6',textStyle:{color:'#e4e6eb'}},
grid:{left:'8%',right:'4%',top:'12%',bottom:'8%'},
xAxis:{type:'category',data:['2025A','2026E','2028E','2030E'],axisLabel:{color:'#9aa1b2'},axisLine:{lineStyle:{color:'#2a2d3a'}}},
yAxis:{type:'value',name:'GW',nameTextStyle:{color:'#9aa1b2'},axisLabel:{color:'#9aa1b2'},splitLine:{lineStyle:{color:'#252836'}}},
series:[{name:'全球海风新增',type:'bar',barWidth:52,data:[9.3,13,22,33],itemStyle:{color:new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'#06b6d4'},{offset:1,color:'#0e7490'}])},label:{show:true,position:'top',color:'#e4e6eb',fontSize:12}}]
});
c2.on('click',function(p){var cats=['2025A','2026E','2028E','2030E'];var k=cats[p.dataIndex];var v=window['D_GLOBAL'][k];if(v)openModal(v[0],v[1],v[2]);});

var c3=echarts.init(gd('chart-invest-compare'));
c3.setOption({
tooltip:{trigger:'axis',axisPointer:{type:'shadow'},backgroundColor:'#252836',borderColor:'#3b82f6',textStyle:{color:'#e4e6eb'}},
grid:{left:'8%',right:'4%',top:'12%',bottom:'8%'},
xAxis:{type:'category',data:['陆上风电','近海风电','深远海风电'],axisLabel:{color:'#9aa1b2'},axisLine:{lineStyle:{color:'#2a2d3a'}}},
yAxis:{type:'value',name:'亿元/GW',nameTextStyle:{color:'#9aa1b2'},axisLabel:{color:'#9aa1b2'},splitLine:{lineStyle:{color:'#252836'}}},
series:[{name:'单位投资',type:'bar',barWidth:56,data:[50,120,155],itemStyle:{color:function(p){return p.dataIndex===0?'#22c55e':p.dataIndex===1?'#3b82f6':'#f59e0b';}},label:{show:true,position:'top',color:'#e4e6eb',fontSize:12,formatter:function(p){return p.value+'亿元/GW';}}}]
});
c3.on('click',function(p){var v=window['D_INVEST'][p.name];if(v)openModal(v[0],v[1],v[2]);});

var c4=echarts.init(gd('chart-offshore-bom'));
c4.setOption({
tooltip:{trigger:'item',formatter:'{b}: {c}% ({d}%)',backgroundColor:'#252836',borderColor:'#3b82f6',textStyle:{color:'#e4e6eb'}},
legend:{orient:'vertical',right:10,top:'middle',textStyle:{color:'#9aa1b2',fontSize:11},itemWidth:12,itemHeight:8},
series:[{type:'pie',radius:['42%','68%'],center:['42%','52%'],label:{color:'#e4e6eb',fontSize:11,formatter:'{b} {c}%'},data:[
{value:38,name:'整机（含塔筒）',itemStyle:{color:'#3b82f6'}},
{value:23,name:'塔基与基础',itemStyle:{color:'#a78bfa'}},
{value:12,name:'施工安装',itemStyle:{color:'#f59e0b'}},
{value:12,name:'海缆',itemStyle:{color:'#06b6d4'}},
{value:8,name:'叶片',itemStyle:{color:'#22c55e'}},
{value:7,name:'其他',itemStyle:{color:'#6b7280'}}
]}]
});
c4.on('click',function(p){var v=window['D_BOM_OFFSHORE'][p.name];if(v)openModal(v[0],v[1],v[2]);});

var c5=echarts.init(gd('chart-onshore-bom'));
c5.setOption({
tooltip:{trigger:'axis',axisPointer:{type:'shadow'},backgroundColor:'#252836',borderColor:'#3b82f6',textStyle:{color:'#e4e6eb'}},
grid:{left:'12%',right:'10%',top:'8%',bottom:'8%'},
xAxis:{type:'value',name:'占整机成本（%）',nameTextStyle:{color:'#9aa1b2'},axisLabel:{color:'#9aa1b2'},splitLine:{lineStyle:{color:'#252836'}}},
yAxis:{type:'category',data:['其他','变流器','轴承','发电机','塔筒','齿轮箱','叶片'],axisLabel:{color:'#9aa1b2'},axisLine:{lineStyle:{color:'#2a2d3a'}}},
series:[{name:'占比',type:'bar',barWidth:20,data:[12.5,5.4,6.0,9.0,11.0,13.5,22.5],itemStyle:{color:new echarts.graphic.LinearGradient(0,0,1,0,[{offset:0,color:'#3b82f6'},{offset:1,color:'#60a5fa'}])},label:{show:true,position:'right',color:'#e4e6eb',fontSize:11,formatter:function(p){return p.value+'%';}}}]
});
var BOMON={'叶片':'叶片','齿轮箱':'齿轮箱','塔筒':'塔筒','发电机':'发电机','轴承':'轴承','变流器':'变流器','其他':'其他'};
c5.on('click',function(p){var v=window['D_BOM_ONSHORE'][p.name];if(v)openModal(v[0],v[1],v[2]);});

var c6=echarts.init(gd('chart-irr-sens'));
var hs=[3000,3100,3200,3300,3400,3500,3600,3700,3800];
function irrLine(e){return hs.map(function(h){return +(e[0]+e[1]*(h-3000)/800).toFixed(1);});}
c6.setOption({
tooltip:{trigger:'axis',backgroundColor:'#252836',borderColor:'#3b82f6',textStyle:{color:'#e4e6eb'}},
legend:{data:['电价 0.30元/kWh','电价 0.35元/kWh','电价 0.40元/kWh','电价 0.45元/kWh'],textStyle:{color:'#9aa1b2',fontSize:11},top:0},
grid:{left:'8%',right:'16%',top:'20%',bottom:'10%'},
xAxis:{type:'category',data:hs,axisLabel:{color:'#9aa1b2'},axisLine:{lineStyle:{color:'#2a2d3a'}},name:'年等效利用小时（h）',nameTextStyle:{color:'#9aa1b2'}},
yAxis:{type:'value',name:'IRR（%）',nameTextStyle:{color:'#9aa1b2'},axisLabel:{color:'#9aa1b2'},splitLine:{lineStyle:{color:'#252836'}}},
series:[
{name:'电价 0.30元/kWh',type:'line',smooth:true,data:irrLine([3.0,2.6]),itemStyle:{color:'#ef4444'},lineStyle:{width:2}},
{name:'电价 0.35元/kWh',type:'line',smooth:true,data:irrLine([4.5,3.0]),itemStyle:{color:'#f59e0b'},lineStyle:{width:2}},
{name:'电价 0.40元/kWh',type:'line',smooth:true,data:irrLine([6.0,3.6]),itemStyle:{color:'#22c55e'},lineStyle:{width:2}},
{name:'电价 0.45元/kWh',type:'line',smooth:true,data:irrLine([7.5,4.2]),itemStyle:{color:'#3b82f6'},lineStyle:{width:2}},
{name:'市场要求回报线',type:'line',data:hs.map(function(){return 6.5;}),lineStyle:{type:'dashed',color:'#9aa1b2'},symbol:'none',tooltip:{show:false},itemStyle:{color:'#9aa1b2'},label:{show:true,position:'right',color:'#9aa1b2',fontSize:10,formatter:'6.5%'}}
],
markLine:undefined
});
c6.on('click',function(p){
if(p.seriesName==='市场要求回报线')return;
var h=hs[p.dataIndex];var raw=Array.isArray(p.value)?p.value[1]:p.value;var v=+raw.toFixed(1);
var name=p.seriesName;var sub=name+' · 利用小时'+h+'h';
var cls=v>=6.5?'（高于6.5%市场要求回报线）':'（低于6.5%市场要求回报线）';
openModal(name,sub,'<p>该组合下IRR约<strong>'+v+'%</strong>'+cls+'。电价每低0.02元/kWh，IRR约下降1.5pct；利用小时每降200h，IRR约下降1pct。</p>');
});

var c7=echarts.init(gd('chart-oem-fin'));
c7.setOption({
tooltip:{trigger:'axis',axisPointer:{type:'shadow'},backgroundColor:'#252836',borderColor:'#3b82f6',textStyle:{color:'#e4e6eb'}},
legend:{data:['营业收入（亿元）','归母净利润（亿元）'],textStyle:{color:'#9aa1b2'},top:0},
grid:{left:'8%',right:'5%',top:'20%',bottom:'8%'},
xAxis:{type:'category',data:['金风科技','明阳智能','三一重能','运达股份','电气风电'],axisLabel:{color:'#9aa1b2'},axisLine:{lineStyle:{color:'#2a2d3a'}}},
yAxis:[{type:'value',name:'亿元',nameTextStyle:{color:'#9aa1b2'},axisLabel:{color:'#9aa1b2'},splitLine:{lineStyle:{color:'#252836'}}}],
series:[
{name:'营业收入（亿元）',type:'bar',barWidth:26,data:[337.39,170.36,106.6,138.25,56.54],itemStyle:{color:new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'#3b82f6'},{offset:1,color:'#1e40af'}])},label:{show:true,position:'top',color:'#e4e6eb',fontSize:10}},
{name:'归母净利润（亿元）',type:'bar',barWidth:26,data:[18.55,1.11,2.33,-2.49,-5.5],itemStyle:{color:function(p){return p.value<0?'#ef4444':'#22c55e';}},label:{show:true,position:function(p){return p.value<0?'bottom':'top';},color:'#e4e6eb',fontSize:10,formatter:function(p){return p.value;}}}
]}
);
c7.on('click',function(p){var v=window['D_OEM'][p.name];if(v)openModal(v[0],v[1],v[2]);});

var c8=echarts.init(gd('chart-valuation'));
c8.setOption({
tooltip:{trigger:'axis',axisPointer:{type:'shadow'},backgroundColor:'#252836',borderColor:'#3b82f6',textStyle:{color:'#e4e6eb'}},
grid:{left:'12%',right:'12%',top:'8%',bottom:'8%'},
xAxis:{type:'value',name:'PE（倍）',nameTextStyle:{color:'#9aa1b2'},axisLabel:{color:'#9aa1b2'},splitLine:{lineStyle:{color:'#252836'}}},
yAxis:{type:'category',data:['三峡能源','亨通光电','中天科技','龙源电力','大金重工','东方电缆','金风科技','新强联'],axisLabel:{color:'#9aa1b2'},axisLine:{lineStyle:{color:'#2a2d3a'}}},
series:[{name:'动态PE',type:'bar',barWidth:18,data:[93.5,38.5,32.3,35.7,25,21.8,20.8,14.5],itemStyle:{color:function(p){return p.value>50?'#ef4444':p.value>30?'#f59e0b':'#22c55e';}},label:{show:true,position:'right',color:'#e4e6eb',fontSize:11,formatter:function(p){return p.value+'x';}}}]
});
c8.on('click',function(p){var v=window['D_VAL'][p.name];if(v)openModal(v[0],v[1],v[2]);});

var c9=echarts.init(gd('chart-layering'));
c9.setOption({
tooltip:{trigger:'item',formatter:function(p){return p.data.name+'<br/>景气确定性：'+p.data.value[0]+'<br/>盈利弹性：'+p.data.value[1];},backgroundColor:'#252836',borderColor:'#3b82f6',textStyle:{color:'#e4e6eb'}},
grid:{left:'10%',right:'12%',top:'10%',bottom:'14%'},
xAxis:{type:'value',name:'景气确定性（订单/格局/政策支撑）',nameLocation:'middle',nameGap:26,nameTextStyle:{color:'#9aa1b2'},min:30,max:100,axisLabel:{color:'#9aa1b2'},splitLine:{lineStyle:{color:'#252836'}}},
yAxis:{type:'value',name:'盈利弹性',nameTextStyle:{color:'#9aa1b2'},min:20,max:90,axisLabel:{color:'#9aa1b2'},splitLine:{lineStyle:{color:'#252836'}}},
series:[{type:'scatter',symbolSize:function(d){return 16+ (d[0]*d[1])/180;},data:[
{value:[85,72],name:'海缆',itemStyle:{color:'#3b82f6'}},
{value:[80,76],name:'塔基基础',itemStyle:{color:'#22c55e'}},
{value:[72,68],name:'轴承',itemStyle:{color:'#a78bfa'}},
{value:[68,62],name:'整机',itemStyle:{color:'#06b6d4'}},
{value:[75,42],name:'叶片',itemStyle:{color:'#f59e0b'}},
{value:[72,52],name:'齿轮箱',itemStyle:{color:'#ec4899'}},
{value:[66,46],name:'铸锻件',itemStyle:{color:'#84cc16'}},
{value:[62,42],name:'变流器',itemStyle:{color:'#14b8a6'}},
{value:[70,32],name:'运营商',itemStyle:{color:'#6b7280'}},
{value:[42,58],name:'漂浮式',itemStyle:{color:'#ef4444'}}
],label:{show:true,position:'right',color:'#e4e6eb',fontSize:11,formatter:function(p){return p.data.name;}}}]
});
c9.on('click',function(p){var v=window['D_LAYER'][p.data.name];if(v)openModal(v[0],v[1],v[2]);});
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
c10.on('click',function(p){var m=p.data;var txt='<p><b>招标均价'+sx[m[0]]+'，原材料综合成本'+sy[m[1]]+'</b></p><p>该组合下整机商净利率约 <b>'+m[2]+'%</b>。'+(m[2]>=8?'盈利显著改善，对应招标价企稳与成本下行的乐观情形。':(m[2]>=2?'盈利微利至正常，为基准偏中性情形。':(m[2]>=0?'接近盈亏平衡，价格战尾部情形。':'净利率为负，整机厂亏损，对应价格战深度出清阶段。')))+'</p><p class="fig-note">模型为示意：基准净利率4%，招标价弹性约±0.35pct/1%，成本弹性约∓0.25pct/1%。</p>';openModal('盈利敏感性组合','整机净利率 '+m[2]+'%',txt);});
window.addEventListener('resize',function(){[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10].forEach(function(c){c.resize();});});
"""

order = ['summary', 'macro', 'policy', 'demand', 'chain', 'diagram', 'value', 'economics', 'stocks', 'mispricing', 'risk']
nav_html = ''.join('<a href="#' + sid + '"' + (' class="active"' if sid == 'summary' else '') + '>' + S[sid][0] + '</a>' for sid in order)
sec_html = '\n'.join('<div class="section" id="' + sid + '">\n' + mark_parse(S[sid][1]) + '\n</div>' for sid in order)

DATA_JS = ''
for _dk in ['D_ANNUAL', 'D_GLOBAL', 'D_INVEST', 'D_BOM_OFFSHORE', 'D_BOM_ONSHORE', 'D_OEM', 'D_VAL', 'D_LAYER', 'D_PARTS']:
    DATA_JS += 'window["' + _dk + '"]=' + json.dumps(globals()[_dk], ensure_ascii=False) + ';\n'

page = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>风电行业研究 · 量增价稳，盈利拐点与出海共振</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230F1117'/%3E%3Ccircle cx='32' cy='32' r='5' fill='%233B82F6'/%3E%3Cpath d='M32 32 L32 12 M32 32 L50 24 M32 32 L47 42 M32 32 L14 26 M32 32 L19 44' stroke='%2360A5FA' stroke-width='4' stroke-linecap='round'/%3E%3C/svg%3E">
<script src="echarts.min.js"></script>
<style>
""" + CSS + """</style>
</head>
<body>
<div class="nav">
""" + nav_html + """
</div>
<div class="container">
""" + sec_html + """

</div>
<div class="modal" id="chartModal">
<div class="modal-box">
<button class="modal-close" onclick="closeModal()">×</button>
<h3 id="modalTitle"></h3>
<div class="modal-sub" id="modalSub"></div>
<div id="modalBody"></div>
</div>
</div>
<script>
""" + FUNC_JS + DATA_JS + CHART_JS2 + """
</script>
</body>
</html>"""

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(page)
print('REPORT OK ->', OUT, os.path.getsize(OUT), 'bytes | sections:', len(S))
