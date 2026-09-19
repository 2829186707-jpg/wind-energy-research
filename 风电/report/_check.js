

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
window["D_ANNUAL"]={"2025A": ["中国风电新增装机结构（2025实际）", "合计约100GW · 全球首个年新增突破100GW市场", "<p>2025年中国新增装机约**100GW**：陆上**93.4GW**、海上**6.6GW**。中国海风新增连续第八年全球第一；沙戈荒大基地与分散式贡献主要增量。</p>"], "2026E": ["中国风电新增装机结构（2026预计）", "合计约115GW · 海风同比+30%", "<p>2026年中国新增装机约**115GW**：陆上**105GW**、海上**10GW**。机制电价竞价落地约**7000万千瓦**装机底盘，海风进入放量爬坡期。</p>"], "十五年均": ["中国风电新增装机结构（十五五年均）", "合计约120GW · 风能北京宣言2.0目标", "<p>“十五五”期间中国风电年新增不低于**1.2亿千瓦**：陆上约**105GW**、海上**15GW**（不低于1500万千瓦）。2030年累计装机**13亿千瓦**、海风累计**1亿千瓦以上**。</p>"]};
window["D_GLOBAL"]={"2025A": ["全球海上风电新增并网（2025实际）", "GWEC口径", "<p>全球海风新增并网**9.3GW**（同比+16%），为历史第三高年度；累计装机**92.5GW**。中国以6.6GW居首，英国、德国、荷兰居欧洲前三。</p>"], "2026E": ["全球海上风电新增并网（2026预计）", "GWEC口径", "<p>全球海风新增约**13GW**。欧洲北海项目集中建设（英国5GW+、荷兰3GW+），中国继续放量，亚太（越南、菲律宾）启动。</p>"], "2028E": ["全球海上风电新增并网（2028预计）", "GWEC口径", "<p>全球海风新增约**22GW**。欧洲大型海上风电集群（1GW+单体项目）密集并网，中国“十五五”海风年增爬坡至15GW附近。</p>"], "2030E": ["全球海上风电新增并网（2030预计）", "GWEC口径", "<p>全球海风新增约**33GW**，海风占风电新增比例升至**16%**。漂浮式开始商业化，亚太与美洲贡献增量。</p>"]};
window["D_INVEST"]={"陆上风电": ["陆上风电单GW单位投资", "约50亿元/GW", "<p>整机（含塔筒）占**40%-45%**、塔筒**10%**、基础**10%-12%**、升压站与送出**15%-20%**、施工**10%**。度电成本约**0.15-0.25元/kWh**，全面平价。</p>"], "近海风电": ["近海风电单GW单位投资", "约120亿元/GW", "<p>整机（含塔筒）占**35%-40%**、塔基与基础**20%-25%**、海缆**10%-15%**、施工**10%-15%**。近海利用小时约**3000-3500h**，度电成本约**0.3-0.4元/kWh**。</p>"], "深远海风电": ["深远海风电单GW单位投资", "约155亿元/GW", "<p>水深50米以上，单桩升级为导管架/漂浮式基础，海缆长度与电压等级提升。单GW投资**130-180亿元**，需漂浮式商业化后进一步降本。</p>"]};
window["D_BOM_OFFSHORE"]={"整机（含塔筒）": ["海上风电整机（含塔筒）", "占单GW投资38% · 约33亿元/GW", "<p>海风含塔筒中标均价约**3280元/kW**。单机容量**11-18MW**为主力，大型化摊薄单位造价；代表：金风/明阳/远景/运达/三一。</p>"], "塔基与基础": ["塔基与基础（单桩/导管架）", "占单GW投资23% · 约24-36亿元/GW", "<p>大金重工（欧洲**29.1%**）、天顺风能、海力风电、泰胜风能。万吨级单桩需深水码头与大型门式起重机，出口毛利率**35%+**。</p>"], "施工安装": ["海上施工安装", "占单GW投资12%", "<p>中国WTIV在册**42艘**，需新增**15-20艘**大吨位船。船机资源是海风装机的真正瓶颈，跟踪吊装进度比招标量更能反映真实放量。</p>"], "海缆": ["海缆（阵列+送出）", "占单GW投资12% · 约12-18亿元/GW", "<p>中天**36%-38%**、东方电缆**25%**、亨通**18%**三强垄断。电压等级从66kV阵列向330kV送出、±525kV直流跃迁，单GW价值量持续提升。</p>"], "叶片": ["海上风电叶片", "占单GW投资8%", "<p>中材科技（国内**28.9%**）+时代新材（**24%**）双寡头。海上叶片长度**110-130米**，碳纤维主梁渗透率提升。</p>"], "其他": ["其他（升压站/变流/勘测等）", "占单GW投资7%", "<p>海上升压站、动态海缆、勘测设计等，随离岸距离增加占比上升。</p>"]};
window["D_BOM_ONSHORE"]={"叶片": ["叶片占整机成本", "22.5% · 价值量最大的单一零部件", "<p>中材科技（全球第一）+时代新材双寡头，毛利率约**18.9%**。碳纤维主梁渗透+海外订单是主要预期差。</p>"], "齿轮箱": ["齿轮箱占整机成本", "13.5% · 单GW约2-2.4亿元", "<p>南高齿**23.4%**+采埃孚**22.7%**+重齿**20.6%**（前三强**66.7%**）。毛利率**25%-30%**，半直驱渗透+海风大兆瓦溢价。</p>"], "塔筒": ["塔筒占整机成本", "11.0% · 单GW约2-2.5亿元", "<p>天顺**21.3%**、大金**17.3%**、泰胜**13.8%**。出口欧洲毛利率**35%+**，欧洲产能缺口3-5年难解。</p>"], "发电机": ["发电机占整机成本", "9.0%", "<p>大型化下发电机单机功率提升，直驱/半直驱路线影响其价值量结构。</p>"], "轴承": ["轴承占整机成本", "6.0% · 单GW约0.8-1.1亿元", "<p>国产化率整体**78.4%**（偏航变桨**91.3%**、主轴**70.5%**）。新强联TRB渗透率**70%+**，齿轮箱轴承国产化是**129亿**市场。</p>"], "变流器": ["变流器占整机成本", "5.4% · 单GW约0.8-1亿元", "<p>禾望电气、阳光电源为第三方龙头，构网型变流器成为沙戈荒基地标配。</p>"], "其他": ["其他（机舱罩/线缆/控制系统等）", "12.5%", "<p>含机舱罩、线缆、控制系统、辅材等。</p>"]};
window["D_OEM"]={"金风科技": ["金风科技 · 整机龙头", "营收337.39亿元 / 归母净利18.55亿元", "<p>营收**337.39亿元**（+18.23%）、归母净利**18.55亿元**（+24.67%）、扣非**20.2亿元**（+47.8%）。动态PE约**20.8倍**，盈利质量行业第一，海风放量、出海兑现与价格企稳。</p>"], "明阳智能": ["明阳智能 · 海上整机龙头", "营收170.36亿元 / 归母净利1.11亿元", "<p>营收**170.36亿元**、净利**1.11亿元**（-81.77%）。海风优势仍在但短期盈利承压，海风放量后盈利拐点期权标的。</p>"], "三一重能": ["三一重能 · 盈利修复标的", "营收106.6亿元 / 归母净利2.33亿元", "<p>营收**106.6亿元**（+24.04%）、净利**2.33亿元**（+10.99%）。毛利率修复与份额提升兼具，估值处于低位。</p>"], "运达股份": ["运达股份 · 份额提升但亏损", "营收138.25亿元 / 归母净利-2.49亿元", "<p>营收**138.25亿元**（+26.9%）但归母净利**-2.49亿元**（由盈转亏）。价格战下盈利承压，需跟踪价格企稳后的盈利修复。</p>"], "电气风电": ["电气风电 · 订单先行", "营收56.54亿元 / 净利亏损", "<p>营收**56.54亿元**（+112.27%）、在手订单**23478.5MW**（+16.66%）。订单先行、利润后至，海风放量是核心催化。</p>"]};
window["D_VAL"]={"金风科技": ["金风科技", "动态PE 20.8倍", "<p>盈利确定性最强的整机龙头：扣非+47.8%、海风+出海结构升级，盈利与估值双修复空间最大。</p>"], "东方电缆": ["东方电缆", "动态PE 21.8倍", "<p>海缆毛利率**33.36%**、在手订单**193亿元**。高压+深远的确定性溢价标的，估值与成长匹配度高。</p>"], "大金重工": ["大金重工", "动态PE 25倍（2026E）", "<p>欧洲海上基础市占**29.1%**居首、自有船队**24艘**（合同**120亿**）、出口单桩毛利率**35%+**，出海弹性最大。</p>"], "新强联": ["新强联", "动态PE 14.5倍", "<p>TRB渗透率**70%+**+齿轮箱轴承国产化（**129亿**市场）双逻辑，2026-2028年PE约**10/8/6倍**。</p>"], "中天科技": ["中天科技", "动态PE 32.3倍", "<p>海缆市占**36%-38%**、掌握**±500kV**柔性直流技术，光通信+海洋双主业。</p>"], "亨通光电": ["亨通光电", "动态PE 38.5倍", "<p>海缆市占**18%**+算力电缆第二曲线，估值含多业务溢价。</p>"], "龙源电力": ["龙源电力", "动态PE 35.7倍", "<p>央企风电运营龙头：营收**146.42亿元**、净利**23.93亿元**，海风核准与大基地开工打开成长空间，盈利稳定。</p>"], "三峡能源": ["三峡能源", "动态PE 93.5倍", "<p>净利**12.19亿元**（含大量在建资产待投产）。装机成长最快，投产兑现后估值有望消化。</p>"]};
window["D_LAYER"]={"海缆": ["海缆", "景气确定性85 · 盈利弹性72", "<p>三强垄断+高压壁垒+深远海量价齐升，是风电确定性溢价最高的环节。</p>"], "塔基基础": ["塔基基础（出海）", "景气确定性80 · 盈利弹性76", "<p>欧洲产能缺口与自有运力构成壁垒，出口毛利率**35%+**，订单排至2027-2028年。</p>"], "轴承": ["轴承（国产替代）", "景气确定性72 · 盈利弹性68", "<p>TRB渗透率**70%+**+齿轮箱轴承国产化，129亿市场是最大替代空间。</p>"], "整机": ["整机（盈利拐点）", "景气确定性68 · 盈利弹性62", "<p>价格企稳、海风放量与出海兑现下，盈利修复弹性最大，但格局波动较大。</p>"], "叶片": ["叶片（双寡头）", "景气确定性75 · 盈利弹性42", "<p>中材+时代新材双寡头，格局稳但盈利弹性偏弱，看碳纤维与海外。</p>"], "齿轮箱": ["齿轮箱（半直驱）", "景气确定性72 · 盈利弹性52", "<p>前三强**66.7%**集中，半直驱渗透+海风大兆瓦溢价。</p>"], "铸锻件": ["铸锻件（大型化）", "景气确定性66 · 盈利弹性46", "<p>日月股份全球**25-30%**，海风大型化提升单GW价值量，核电第二曲线。</p>"], "变流器": ["变流器（构网型）", "景气确定性62 · 盈利弹性42", "<p>构网型成为沙戈荒标配，IGBT国产化与SiC渗透带来成本下行。</p>"], "运营商": ["运营商（类公用）", "景气确定性70 · 盈利弹性32", "<p>股息率、装机成长与绿电/CCER弹性，盈利稳定。</p>"], "漂浮式": ["漂浮式（远期期权）", "景气确定性42 · 盈利弹性58", "<p>2028-2030年商业化打开深远海**70%**空间，当前尚未定价。</p>"]};
window["D_PARTS"]={"blade": ["叶片", "占整机成本20%-25% · 陆上单GW约3-4亿元", "<img src=\"assets/parts/blade.jpg\" class=\"part-img\"><p>占整机成本**20%-25%**（陆上单GW约**3-4亿元**）。中材科技（全球第一、国内**28.9%**）+时代新材（约**24%**）双寡头，毛利率约**18.9%**。大兆瓦化后海上叶片长度增至**110-130米**，碳纤维主梁渗透率提升，海外订单（欧洲订单增**30%**）打开第二曲线。</p><p class=\"cmp-title\">主要参与公司产品对比</p><div class=\"tbl-wrap\"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>中材科技</td><td>百米级玻纤/碳纤维主梁叶片</td><td>全球第一、国内28.9%</td></tr><tr><td>时代新材</td><td>海上大兆瓦叶片</td><td>国内约24%</td></tr></table></div>"], "gearbox": ["齿轮箱", "占整机成本12%-15% · 单GW约2-2.4亿元", "<img src=\"assets/parts/gearbox.jpg\" class=\"part-img\"><p>南高齿**23.4%**+采埃孚**22.7%**+重齿**20.6%**，前三强集中度**66.7%**，毛利率**25%-30%**。半直驱渗透+大兆瓦海风齿轮箱溢价+海外主机厂采购放量是主要预期差。</p><p class=\"cmp-title\">主要参与公司产品对比</p><div class=\"tbl-wrap\"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>南高齿</td><td>双馈/半直驱主齿轮箱</td><td>23.4%份额</td></tr><tr><td>采埃孚</td><td>风电主齿轮箱</td><td>22.7%份额</td></tr><tr><td>重齿</td><td>大型风电齿轮箱</td><td>20.6%份额</td></tr></table></div>"], "generator": ["发电机", "占整机成本约9%", "<img src=\"assets/parts/generator.jpg\" class=\"part-img\"><p>大型化下单机功率持续提升（海上**11-18MW**），直驱（永磁同步）与半直驱（中速永磁）路线占比上升。金风、明阳以自研为主，中车株洲电机、东电电机等供应部分整机商。</p><p class=\"cmp-title\">主要参与公司产品对比</p><div class=\"tbl-wrap\"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>中车株洲电机</td><td>永磁直驱/半直驱发电机</td><td>第三方龙头</td></tr><tr><td>东方电机</td><td>大型风力发电机</td><td>配套整机商</td></tr><tr><td>金风/明阳</td><td>自研发电机</td><td>垂直一体化</td></tr></table></div>"], "bearing": ["轴承", "占整机成本5%-7% · 单GW约0.8-1.1亿元", "<img src=\"assets/parts/bearing.jpg\" class=\"part-img\"><p>国产化率整体**78.4%**（偏航变桨**91.3%**、主轴**70.5%**）。新强联TRB（双列圆锥滚子）渗透率**70%+**，洛轴、瓦轴跟进；齿轮箱轴承国产化（**129亿**市场）是最大替代空间。</p><p class=\"cmp-title\">主要参与公司产品对比</p><div class=\"tbl-wrap\"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>新强联</td><td>TRB主轴轴承</td><td>渗透率70%+</td></tr><tr><td>洛轴</td><td>偏航变桨/主轴轴承</td><td>国产化主力</td></tr><tr><td>瓦轴</td><td>大型风电轴承</td><td>国产化跟随</td></tr></table></div>"], "converter": ["变流器", "占整机成本4.8%-6% · 单GW约0.8-1亿元", "<img src=\"assets/parts/converter.jpg\" class=\"part-img\"><p>禾望电气、阳光电源为第三方龙头，金风/远景/明阳自研比例上升。构网型变流器成为沙戈荒大基地与新型电力系统标配；IGBT国产化与SiC渗透带来成本下行。</p><p class=\"cmp-title\">主要参与公司产品对比</p><div class=\"tbl-wrap\"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>禾望电气</td><td>风电变流器</td><td>第三方龙头</td></tr><tr><td>阳光电源</td><td>风电变流器</td><td>头部供应商</td></tr><tr><td>金风/远景</td><td>自研变流器</td><td>垂直一体化</td></tr></table></div>"], "nacelle": ["机舱总成", "机舱罩+主轴+齿轮箱+发电机等核心总成", "<img src=\"assets/parts/nacelle.jpg\" class=\"part-img\"><p>机舱内集成主轴、齿轮箱、发电机、变流器、控制系统等核心部件，是整机技术含量最高的总成。机舱内细色块对应**齿轮箱/轴承/发电机/变流器**，可分别查看。</p><p class=\"cmp-title\">主要参与公司产品对比</p><div class=\"tbl-wrap\"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>金风科技</td><td>直驱/半直驱机舱总成</td><td>整机龙头</td></tr><tr><td>明阳智能</td><td>海上机舱总成</td><td>海风领先</td></tr><tr><td>远景能源</td><td>智能机舱总成</td><td>全球出货前三</td></tr></table></div>"], "install": ["装机与基础（细分选择）", "点击下方环节查看具体分析", "<div class=\"sub-list\"><button onclick=\"showPart('tower')\">塔筒</button><button onclick=\"showPart('flange')\">法兰</button><button onclick=\"showPart('monopile')\">单桩</button><button onclick=\"showPart('jacket')\">导管架</button><button onclick=\"showPart('foundation')\">陆上基础</button></div>"], "tower": ["塔筒", "占整机成本10%-12% · 单GW约2-2.5亿元；海风塔筒+基础占20%-30%", "<img src=\"assets/parts/tower.jpg\" class=\"part-img\"><p>天顺**21.3%**、大金**17.3%**、泰胜**13.8%**（CR5约**55%-60%**）。大兆瓦化提升单机塔筒重量与价值量；出口欧洲塔筒毛利率**35%-39%**。</p><p class=\"cmp-title\">主要参与公司产品对比</p><div class=\"tbl-wrap\"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>天顺风能</td><td>陆海塔筒</td><td>21.3%份额</td></tr><tr><td>大金重工</td><td>塔筒+基础</td><td>17.3%份额</td></tr><tr><td>泰胜风能</td><td>陆海塔筒</td><td>13.8%份额</td></tr></table></div>"], "flange": ["法兰", "塔筒节间/塔筒-基础连接锻件 · 恒润股份市占约9.4%", "<img src=\"assets/parts/flange.jpg\" class=\"part-img\"><p>法兰是塔筒节间与塔筒-基础连接的关键锻件，恒润股份为龙头（市占率约**9.4%**）并延伸轴承业务。出海与大型化提升单GW价值量。</p><p class=\"cmp-title\">主要参与公司产品对比</p><div class=\"tbl-wrap\"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>恒润股份</td><td>风电法兰+轴承</td><td>市占约9.4%</td></tr><tr><td>大金重工</td><td>塔筒+法兰集成</td><td>欧洲基础29.1%</td></tr><tr><td>天顺风能</td><td>塔筒+法兰集成</td><td>全球塔筒龙头</td></tr></table></div>"], "monopile": ["单桩基础（海上）", "占海风单GW投资20%-25% · 出海第一赛道", "<img src=\"assets/parts/monopile.jpg\" class=\"part-img\"><p>大金重工欧洲海上基础市占**29.1%**居首、自有船队**24艘**（合同约**120亿**）、出口单桩毛利率**35%+**；天顺、海力、泰胜跟随。万吨级单桩需深水码头+大型门式起重机，出口资质稀缺。</p><p class=\"cmp-title\">主要参与公司产品对比</p><div class=\"tbl-wrap\"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>大金重工</td><td>海上单桩</td><td>欧洲29.1%居首</td></tr><tr><td>天顺风能</td><td>单桩/导管架</td><td>出口主力</td></tr><tr><td>海力风电</td><td>海上基础</td><td>跟随放量</td></tr></table></div>"], "jacket": ["导管架基础（海上）", "适用于水深40-60米 · 价值量高于单桩", "<img src=\"assets/parts/jacket.jpg\" class=\"part-img\"><p>随水深增加，导管架/吸力筒基础占比提升。欧洲北海多采用导管架，中国企业导管架产能与出口订单同步放量，是迈向深远海的重要基础形式。</p><p class=\"cmp-title\">主要参与公司产品对比</p><div class=\"tbl-wrap\"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>海力风电</td><td>导管架/吸力筒</td><td>海上基础专精</td></tr><tr><td>泰胜风能</td><td>导管架+塔筒</td><td>多品类布局</td></tr><tr><td>大金重工</td><td>导管架出口</td><td>欧洲订单</td></tr></table></div>"], "foundation": ["陆上基础", "混凝土扩展基础/锚栓 · 占陆上投资10%-12%", "<img src=\"assets/parts/foundation.jpg\" class=\"part-img\"><p>陆上风机基础以混凝土扩展基础与岩石锚杆基础为主，占陆上单GW投资约**10%-12%**。沙戈荒地区采用预应力锚栓基础，随大兆瓦机组载荷提升，基础造价上行。</p><p class=\"cmp-title\">主要参与公司产品对比</p><div class=\"tbl-wrap\"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>中国能建</td><td>风电基础EPC</td><td>央企施工</td></tr><tr><td>中国电建</td><td>风电基础施工</td><td>央企施工</td></tr><tr><td>中交集团</td><td>基础+海工施工</td><td>一体化</td></tr></table></div>"], "cable": ["海缆（阵列+送出）", "占海风单GW投资10%-15% · 约12-18亿元/GW", "<img src=\"assets/parts/cable.jpg\" class=\"part-img\"><p>中天**36%-38%**、东方电缆**25%**、亨通**18%**三强垄断，三家具备**500kV**交付能力。东方电缆海缆毛利率**33.36%**、在手订单**193亿**。电压等级从66kV阵列→330kV送出→±525kV直流跃迁，单GW价值量持续提升。</p><p class=\"cmp-title\">主要参与公司产品对比</p><div class=\"tbl-wrap\"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>中天科技</td><td>±500kV柔性直流海缆</td><td>市占36%-38%</td></tr><tr><td>东方电缆</td><td>330kV/500kV海缆</td><td>毛利率33.36%、订单193亿</td></tr><tr><td>亨通光电</td><td>高压海缆</td><td>市占约18%</td></tr></table></div>"], "substation": ["海上升压站", "占海风投资约4%-5% · 随离岸距离提升价值量", "<img src=\"assets/parts/substation.jpg\" class=\"part-img\"><p>海上升压站将阵列电压升压后经送出缆上网，随离岸距离与场址容量提升，500kV/±525kV送出成为主流，升压站价值量同步提升。代表：特变电工、中天科技（海缆+电气设备协同）。</p><p class=\"cmp-title\">主要参与公司产品对比</p><div class=\"tbl-wrap\"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>特变电工</td><td>海上升压站主变压器</td><td>变压器龙头</td></tr><tr><td>中天科技</td><td>海缆+电气设备协同</td><td>海缆龙头</td></tr><tr><td>正泰电气</td><td>升压站成套设备</td><td>头部供应商</td></tr></table></div>"], "installation": ["施工安装（船机）", "占海风投资10%-15% · 船机是瓶颈", "<img src=\"assets/parts/installation.jpg\" class=\"part-img\"><p>中国WTIV在册**42艘**，需新增**15-20艘**大吨位船。船机资源是海风装机的真正瓶颈，跟踪吊装进度比招标量更能反映真实放量。受益：广州打捞局、中交系统、龙源振华。</p><p class=\"cmp-title\">主要参与公司产品对比</p><div class=\"tbl-wrap\"><table><tr><th>公司</th><th>核心产品</th><th>关键数据</th></tr><tr><td>广州打捞局</td><td>自升式风电安装船</td><td>WTIV运营</td></tr><tr><td>中交系统</td><td>海上风电施工总包</td><td>船队+施工</td></tr><tr><td>龙源振华</td><td>海上风电安装</td><td>专业安装</td></tr></table></div>"]};

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

