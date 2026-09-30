#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v2 major upgrade: whole-Bible depth, geography, kings memory, viz, CSS dynamics."""
from pathlib import Path
import re

ROOT = Path("/workspace/reformed-bible-study-continental-20260930-v2")
HTML = ROOT / "index.html"
CSS = ROOT / "assets" / "styles.css"
JS = ROOT / "assets" / "app.js"
PKG = ROOT / "package.json"
README = ROOT / "README.md"

html = HTML.read_text(encoding="utf-8")
css = CSS.read_text(encoding="utf-8")

# ── meta / title / version ───────────────────────────────────
html = html.replace(
    '<meta name="description" content="欧陆改革宗整本圣经研读：三项联合信条与三大普世信经框架下的救赎历史、圣约神学、诸王时代与分卷要点。" />',
    '<meta name="description" content="欧陆改革宗整本圣经研读 v2（2026-09-30）：救赎历史时间线、地理文化背景、圣约与圣经神学、诸王纪年记忆、66卷速学；三项联合信条与三大普世信经。" />',
)
html = html.replace(
    "<title>欧陆改革宗 · 整本圣经研读</title>",
    "<title>欧陆改革宗 · 整本圣经研读 v2 · 20260930</title>",
)
html = html.replace(
    '<span class="brand-title">欧陆改革宗 · 整本圣经研读</span>\n          <span class="brand-sub">三项联合信条 · 三大普世信经 · 以基督为中心</span>',
    '<span class="brand-title">欧陆改革宗 · 整本圣经研读</span>\n          <span class="brand-sub">v2 · 20260930 · 三项联合信条 · 三大普世信经</span>',
)
html = html.replace(
    "<h1>整本圣经 · 欧陆改革宗研读</h1>\n  <p class=\"hero-brand-line\">三项联合信条 · 三大普世信经 · 以基督为中心</p>",
    """<h1>整本圣经 · 欧陆改革宗研读 <span class="ver-badge">v2</span></h1>
  <p class="hero-brand-line">2026-09-30 · 三项联合信条 · 三大普世信经 · 以基督为中心</p>""",
)

# add chips for new sections
if 'href="#sec-geo"' not in html:
    html = html.replace(
        '<a class="chip chip-rose" href="#sec-2-2"><span class="chip-ico" aria-hidden="true">📱</span>手机速记</a>',
        '''<a class="chip chip-rose" href="#sec-2-2"><span class="chip-ico" aria-hidden="true">📱</span>手机速记</a>
    <a class="chip chip-blue" href="#sec-geo"><span class="chip-ico" aria-hidden="true">🌍</span>地理文化</a>
    <a class="chip chip-amber" href="#sec-storyline"><span class="chip-ico" aria-hidden="true">📖</span>故事线</a>
    <a class="chip chip-teal" href="#sec-6-dated"><span class="chip-ico" aria-hidden="true">🔢</span>诸王纪年</a>''',
    )

# ── NEW SECTION: Storyline (insert after one-line section essence or before sec-0) ──
STORYLINE = r'''
<!-- ========== 故事线 · 前因后果 ========== -->
<section class="mod-storyline" id="s-storyline">
  <h2 id="sec-storyline">📖 救赎故事线：前因 → 内容 → 后果 → 应用</h2>
  <p>整本圣经不是零散格言集，而是<strong>同一救赎故事</strong>在真实地理与年代中展开。读每一卷先问：<span class="mark-history">前因</span>（为何此时此地需要这卷？）→ <span class="mark-core">内容</span>（神说了/做了什么？）→ <span class="mark-christ">基督枢纽</span> → <span class="mark-apply">应用</span>（教会与个人如何回应）。</p>

  <div class="storyline-flow" aria-label="故事线八幕">
    <div class="sl-act sl-create"><span class="sl-n">1</span><strong>创造</strong><small>美善秩序<br/>人有神形象</small></div>
    <div class="sl-arrow" aria-hidden="true">→</div>
    <div class="sl-act sl-fall"><span class="sl-n">2</span><strong>堕落</strong><small>罪入世界<br/>行为之约破碎</small></div>
    <div class="sl-arrow" aria-hidden="true">→</div>
    <div class="sl-act sl-promise"><span class="sl-n">3</span><strong>应许</strong><small>女人后裔<br/>恩典之约显明</small></div>
    <div class="sl-arrow" aria-hidden="true">→</div>
    <div class="sl-act sl-israel"><span class="sl-n">4</span><strong>以色列</strong><small>族长→出埃及<br/>西奈→国度</small></div>
    <div class="sl-arrow" aria-hidden="true">→</div>
    <div class="sl-act sl-exile"><span class="sl-n">5</span><strong>审判</strong><small>分裂被掳<br/>约咒诅兑现</small></div>
    <div class="sl-arrow" aria-hidden="true">→</div>
    <div class="sl-act sl-return"><span class="sl-n">6</span><strong>余民</strong><small>归回重建<br/>两约之间</small></div>
    <div class="sl-arrow" aria-hidden="true">→</div>
    <div class="sl-act sl-christ"><span class="sl-n">7</span><strong>基督</strong><small>成全律法先知<br/>新约宝血</small></div>
    <div class="sl-arrow" aria-hidden="true">→</div>
    <div class="sl-act sl-end"><span class="sl-n">8</span><strong>成全</strong><small>教会宣教<br/>新天新地</small></div>
  </div>

  <h3 id="sec-storyline-mind">故事线思维导图（Mermaid）</h3>
  <div class="mermaid-wrap card">
    <pre class="mermaid">
mindmap
  root((整本圣经<br/>一条救赎故事))
    创造与堕落
      创1–2 美善
      创3 堕落与敌意
      行为之约破碎
    应许与族长
      创3:15 后裔
      挪亚 / 亚伯拉罕
      以信称义范式
    出埃及与西奈
      先救赎后律法
      会幕同在
      申命记评分册
    国度与诸王
      大卫之约
      931 分裂
      722 / 586
    先知与被掳
      约的检察官
      新心新约
      人子得国
    基督与教会
      成全影儿
      圣灵宣教
      已然未济
    终末
      再来审判
      身体复活
      新耶路撒冷
    </pre>
  </div>

  <div class="card-grid cols-2">
    <div class="card card-gold">
      <span class="card-tag">为何这样写？</span>
      <h4>作者意图与读者处境</h4>
      <p class="mb-0">每卷都有历史听众：被掳余民需要谱系与圣殿（代上下）；受压教会需要十架智慧（林前）；受试探退回礼仪者需要「更美」论证（来）。先问「当时为何需要」，再问「今日如何应用」——避免把经文当心理鸡汤。</p>
    </div>
    <div class="card">
      <span class="card-tag mark-creed">信条校准</span>
      <h4>比利时 2–7 · 海德堡 19 · 多特</h4>
      <p class="mb-0">圣经充足、清晰、自我解释；圣灵藉圣言重生信心；拣选与坚忍保证故事有主角与结局——不是人的宗教进化，而是神主动立约施行救赎（比16–17；多特第一、五项）。</p>
    </div>
  </div>

  <div class="essence-block open-essence">
    <h4>故事线精髓（常开）</h4>
    <ul class="essence-list">
      <li><span class="mark-history">前因</span> 创造美善 → 人违约 → 死亡与分散进入历史。</li>
      <li><span class="mark-core">核心</span> 神不以毁灭终结，而以恩典之约应许中保，在以色列影儿中预演。</li>
      <li><span class="mark-hub">枢纽</span> 基督的生死复活：影儿成实体，咒诅被担当，新约立定。</li>
      <li><span class="mark-apply">应用</span> 读经、讲道、辅导皆沿故事线：显罪（律法）→ 指向基督（福音）→ 感恩顺服（成圣）。</li>
    </ul>
  </div>
</section>
'''

# Insert storyline before sec-0 section
if 'id="sec-storyline"' not in html:
    html = html.replace(
        '<!-- ========== 0 导论 ========== -->',
        STORYLINE + '\n<!-- ========== 0 导论 ========== -->',
    )
    # fallback if comment differs
    if 'id="sec-storyline"' not in html:
        html = html.replace(
            '<h2 id="sec-0">📖 0. 导论：如何读整本圣经</h2>',
            STORYLINE + '\n<section class="mod-intro" id="s0">\n  <h2 id="sec-0">📖 0. 导论：如何读整本圣经</h2>',
            1,
        )
        # That might break structure - check. Better find s0 section start.
        # Actually let's find the section containing sec-0
        pass

# Fix potential double-open if fallback messed up - verify later

# ── NEW SECTION: Geography & culture (after timeline / before covenants) ──
GEO = r'''
<!-- ========== 地理与历史文化 ========== -->
<section class="mod-geo" id="s-geo">
  <h2 id="sec-geo">🌍 地理 · 历史 · 文化背景</h2>
  <p>圣经事件钉在真实地图与帝国年表上。地理帮助理解「为何这条路、这座城、这场战争」；文化背景防止把古代近东硬套成现代民主或心理自助。改革宗坚持<strong>文法—历史释经</strong>：先作者原意，再基督中心的整本正典综合（比2–7；海德堡 19）。</p>

  <h3 id="sec-geo-map">新月沃地与以色列示意（SVG）</h3>
  <div class="card map-card">
    <svg class="map-svg-lg geo-svg" viewBox="0 0 640 360" role="img" aria-label="古代近东示意地图：埃及、迦南、美索不达米亚、亚述、巴比伦">
      <defs>
        <linearGradient id="seaG" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a3a5c"/><stop offset="100%" stop-color="#0d2137"/></linearGradient>
        <linearGradient id="landG" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#2a3d28"/><stop offset="100%" stop-color="#1a2a1c"/></linearGradient>
      </defs>
      <rect width="640" height="360" fill="url(#seaG)" rx="12"/>
      <!-- Mediterranean -->
      <ellipse cx="70" cy="180" rx="90" ry="140" fill="#0a2844" opacity=".85"/>
      <text x="40" y="170" fill="#6ba3e0" font-size="11">地中海</text>
      <!-- Egypt -->
      <path d="M90,260 Q120,220 150,250 L160,320 L80,330 Z" fill="#c9a227" opacity=".35" stroke="#c9a227" stroke-width="1.5"/>
      <text x="100" y="300" fill="#f0d878" font-size="13" font-weight="700">埃及</text>
      <text x="95" y="316" fill="#b4c4da" font-size="9">出埃及起点</text>
      <!-- Canaan / Israel strip -->
      <path d="M155,140 L185,120 L200,200 L190,260 L160,250 Z" fill="#d4af37" opacity=".45" stroke="#f0d878" stroke-width="2"/>
      <text x="168" y="185" fill="#fff" font-size="12" font-weight="700">迦南</text>
      <text x="162" y="200" fill="#f0d878" font-size="9">以色列/犹大</text>
      <!-- markers -->
      <circle cx="175" cy="155" r="4" fill="#6ba3e0"/><text x="182" y="158" fill="#8bb8e8" font-size="9">加利利</text>
      <circle cx="178" cy="195" r="4" fill="#e8a85c"/><text x="185" y="198" fill="#f0d0a0" font-size="9">撒玛利亚</text>
      <circle cx="180" cy="225" r="5" fill="#d4af37"/><text x="188" y="228" fill="#f0d878" font-size="10" font-weight="700">耶路撒冷</text>
      <!-- Sinai -->
      <circle cx="145" cy="275" r="3" fill="#5ec4c0"/><text x="150" y="278" fill="#8fd8d4" font-size="9">西奈</text>
      <!-- Mesopotamia arc -->
      <path d="M220,80 Q350,40 480,90 Q520,140 500,200 Q450,160 350,150 Q280,140 220,120 Z" fill="#3d9a6a" opacity=".25" stroke="#3d9a6a" stroke-width="1.5"/>
      <text x="320" y="100" fill="#a8dfc4" font-size="12" font-weight="700">新月沃地</text>
      <!-- Assyria -->
      <rect x="300" y="55" width="90" height="40" rx="6" fill="#5b8fd9" opacity=".35" stroke="#5b8fd9"/>
      <text x="312" y="80" fill="#b8d4f0" font-size="12" font-weight="700">亚述</text>
      <text x="308" y="92" fill="#7e92ad" font-size="8">→722 灭北国</text>
      <!-- Babylon -->
      <rect x="400" y="120" width="100" height="45" rx="6" fill="#c45c5c" opacity=".35" stroke="#c45c5c"/>
      <text x="415" y="145" fill="#f0b8b8" font-size="12" font-weight="700">巴比伦</text>
      <text x="410" y="158" fill="#7e92ad" font-size="8">→586 灭南国</text>
      <!-- Persia -->
      <rect x="480" y="80" width="110" height="40" rx="6" fill="#3d9a6a" opacity=".3" stroke="#3d9a6a"/>
      <text x="500" y="105" fill="#a8dfc4" font-size="12" font-weight="700">波斯</text>
      <text x="490" y="117" fill="#7e92ad" font-size="8">538 归回诏令</text>
      <!-- Exile arrows -->
      <path d="M200,170 Q280,130 330,85" fill="none" stroke="#5b8fd9" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#arr)"/>
      <path d="M195,230 Q320,220 420,150" fill="none" stroke="#c45c5c" stroke-width="2" stroke-dasharray="4 3"/>
      <text x="250" y="125" fill="#5b8fd9" font-size="9">北国被掳</text>
      <text x="280" y="210" fill="#c45c5c" font-size="9">南国被掳</text>
      <!-- Dead Sea / Jordan -->
      <ellipse cx="195" cy="245" rx="6" ry="18" fill="#1a5080" opacity=".8"/>
      <text x="205" y="250" fill="#6ba3e0" font-size="8">死海</text>
      <!-- legend -->
      <text x="20" y="350" fill="#7e92ad" font-size="10">示意用教学图 · 非精确投影 · 年代为常用教学概数</text>
    </svg>
  </div>

  <h3 id="sec-geo-regions">关键地带速记</h3>
  <div class="table-wrap">
    <table class="data-table geo-table">
      <thead><tr><th>地带</th><th>为何重要</th><th>关键经文节点</th><th>记忆钩</th></tr></thead>
      <tbody>
        <tr><td>埃及</td><td>为奴与救赎舞台；粮仓与试探「回埃及」</td><td>出1–15；太2逃埃及</td><td>先救赎后律法</td></tr>
        <tr><td>西奈 / 旷野</td><td>立约、会幕、试验信心</td><td>出19–40；民；申</td><td>云柱火柱</td></tr>
        <tr><td>迦南 / 山地</td><td>应许之地；圣战与产业</td><td>书；士；撒</td><td>约旦河东/西</td></tr>
        <tr><td>耶路撒冷</td><td>圣殿、大卫宝座、十架与五旬节</td><td>撒下5–7；王上；四福音；徒</td><td>锡安·圣城</td></tr>
        <tr><td>撒玛利亚</td><td>北国首都区；后混杂民；耶稣越过隔阂</td><td>王上12；约4；徒8</td><td>分裂伤疤</td></tr>
        <tr><td>加利利</td><td>外邦加利利；主的事奉基地</td><td>赛9；太4；可</td><td>渔夫门徒</td></tr>
        <tr><td>美索不达米亚</td><td>亚伯拉罕故乡；亚述/巴比伦帝国心</td><td>创11–12；王下17/25；但</td><td>两河流域</td></tr>
        <tr><td>小亚 / 希腊 / 罗马</td><td>宣教大道；书信受众世界</td><td>徒13–28；启1–3</td><td>直到地极</td></tr>
      </tbody>
    </table>
  </div>

  <h3 id="sec-geo-empires">帝国色码与文化冲击</h3>
  <div class="empire-strip" aria-label="帝国色码">
    <div class="emp emp-eg"><strong>埃及</strong><span>压迫→逾越</span></div>
    <div class="emp emp-as"><strong>亚述</strong><span>722 北亡</span></div>
    <div class="emp emp-bb"><strong>巴比伦</strong><span>586 南亡</span></div>
    <div class="emp emp-pe"><strong>波斯</strong><span>538 归回</span></div>
    <div class="emp emp-gr"><strong>希腊</strong><span>两约间文化</span></div>
    <div class="emp emp-rm"><strong>罗马</strong><span>基督降生<br/>宣教大道</span></div>
  </div>
  <div class="card-grid cols-3">
    <div class="card">
      <span class="card-tag">📜 文体</span>
      <h4>叙事 · 律法 · 诗歌 · 先知 · 书信 · 启示</h4>
      <p class="mb-0">文体决定读法：叙事看情节与神学评价（申命记视角）；律法看约结构；诗歌看平行体与意象；先知看诉讼与应许；书信看论证；启示看象征与旧约回响——勿把启示录当报纸密码。</p>
    </div>
    <div class="card">
      <span class="card-tag">🏛 文化</span>
      <h4>盟约格式 · 圣战 · 圣殿</h4>
      <p class="mb-0">古代宗主权条约帮助理解申命记结构；「圣战」是神审判迦南恶贯满盈的独特历史命令，不可直接复制为今日暴力；圣殿是同在与祭的中心，新约成全为基督与教会（约2；弗2）。</p>
    </div>
    <div class="card">
      <span class="card-tag mark-warn">警戒</span>
      <h4>反两种极端</h4>
      <p class="mb-0">拒自由派否认神迹与预言；亦拒不顾语境的随意寓意与「为我私用」。文法历史 → 正典基督中心 → 教会应用（海德堡 19、21）。</p>
    </div>
  </div>

  <h3 id="sec-geo-flow">地理如何推动故事（Mermaid）</h3>
  <div class="mermaid-wrap card">
    <pre class="mermaid">
flowchart LR
  A["吾珥 / 哈兰<br/>呼召亚伯拉罕"] --> B["迦南寄居"]
  B --> C["下埃及<br/>约瑟护理"]
  C --> D["出埃及<br/>过红海"]
  D --> E["西奈立约<br/>会幕"]
  E --> F["征服迦南<br/>分地"]
  F --> G["耶路撒冷<br/>圣殿与宝座"]
  G --> H["被掳<br/>亚述/巴比伦"]
  H --> I["归回重建"]
  I --> J["加利利→耶路撒冷<br/>十架与空墓"]
  J --> K["直到地极<br/>罗马与万国"]
  style G fill:#c9a227,color:#1a1200
  style J fill:#b39ddb,color:#1a1200
  style K fill:#3d9a6a,color:#04140c
    </pre>
  </div>
</section>
'''

if 'id="sec-geo"' not in html:
    # insert before covenants section (sec-3)
    if '<!-- ========== 3 圣约' in html:
        html = html.replace('<!-- ========== 3 圣约', GEO + '\n<!-- ========== 3 圣约', 1)
    elif 'id="sec-3"' in html:
        html = html.replace(
            '<h2 id="sec-3">📜 3. 圣约神学核心</h2>',
            GEO + '\n<section class="mod-covenant" id="s3">\n  <h2 id="sec-3">📜 3. 圣约神学核心</h2>',
            1,
        )

# ── Expand timeline section with more dated nodes ──
TIMELINE_EXTRA = r'''
  <h3 id="sec-2-dated-nodes">关键年代节点（教学概数）</h3>
  <p>记年代不是考古竞赛，而是把<strong>约的奖惩</strong>钉在历史上：分裂、灭国、归回都有日期可记，方便把列王、先知、被掳串成一条因果链。</p>
  <div class="dated-nodes-grid">
    <div class="dn dn-gold"><span class="dn-y">约前 2000s</span><span class="dn-t">族长时代</span><span class="dn-n">亚伯拉罕之约 · 以信称义</span></div>
    <div class="dn dn-gold"><span class="dn-y">约前 1446/1250</span><span class="dn-t">出埃及（两说）</span><span class="dn-n">先救赎后律法</span></div>
    <div class="dn dn-gold"><span class="dn-y">约前 1050</span><span class="dn-t">扫罗作王</span><span class="dn-n">求王显不信</span></div>
    <div class="dn dn-gold"><span class="dn-y">约前 1010</span><span class="dn-t">大卫作王</span><span class="dn-n">大卫之约</span></div>
    <div class="dn dn-gold"><span class="dn-y">约前 970</span><span class="dn-t">所罗门</span><span class="dn-n">建殿 · 心偏邪</span></div>
    <div class="dn dn-split"><span class="dn-y">前 931</span><span class="dn-t">王国分裂</span><span class="dn-n">罗波安 / 耶罗波安</span></div>
    <div class="dn dn-north"><span class="dn-y">前 722</span><span class="dn-t">北国灭亡</span><span class="dn-n">亚述 · 金牛犊后果</span></div>
    <div class="dn dn-south"><span class="dn-y">前 586</span><span class="dn-t">南国灭亡</span><span class="dn-n">巴比伦 · 圣殿毁</span></div>
    <div class="dn dn-return"><span class="dn-y">前 538</span><span class="dn-t">古列诏令</span><span class="dn-n">首次归回</span></div>
    <div class="dn dn-return"><span class="dn-y">前 516</span><span class="dn-t">第二圣殿</span><span class="dn-n">哈该 / 撒迦利亚</span></div>
    <div class="dn dn-return"><span class="dn-y">前 458/445</span><span class="dn-t">以斯拉 / 尼希米</span><span class="dn-n">律法与城墙</span></div>
    <div class="dn dn-silence"><span class="dn-y">约前 400–5</span><span class="dn-t">两约之间</span><span class="dn-n">希腊 → 罗马</span></div>
    <div class="dn dn-christ"><span class="dn-y">约前 4–30s</span><span class="dn-t">道成肉身</span><span class="dn-n">十架 · 复活 · 升天</span></div>
    <div class="dn dn-church"><span class="dn-y">约 30/33</span><span class="dn-t">五旬节</span><span class="dn-n">教会诞生</span></div>
    <div class="dn dn-church"><span class="dn-y">约 49–67</span><span class="dn-t">宣教与书信</span><span class="dn-n">直到地极</span></div>
    <div class="dn dn-end"><span class="dn-y">将来</span><span class="dn-t">再来与新造</span><span class="dn-n">已然未济成全</span></div>
  </div>
'''

if 'id="sec-2-dated-nodes"' not in html:
    # insert before phone memory sec-2-2 or after visual timeline
    if 'id="sec-2-2"' in html:
        html = html.replace(
            '<h3 id="sec-2-2">手机速记</h3>',
            TIMELINE_EXTRA + '\n  <h3 id="sec-2-2">手机速记</h3>',
            1,
        )
    elif 'id="sec-2-1"' in html:
        # after mermaid timeline
        html = html.replace(
            '<h3 id="sec-2-1">救赎历史总流程（Mermaid）</h3>',
            '<h3 id="sec-2-1">救赎历史总流程（Mermaid）</h3>',
            1,
        )
        # find end of that mermaid block - easier insert before sec-3 if geo already took that
        pass

# ── Kings dated memory (major) ──
KINGS_DATED = r'''
  <h3 id="sec-6-dated">🔢 诸王纪年记忆枢纽（必背）</h3>
  <p>用五个「钉」把南北国钉牢，再挂上改革君王与先知。数字用教学常用年表（有数十年学术浮动，不影响神学因果）。</p>

  <div class="kings-nail-row">
    <div class="knail kn-split"><div class="kn-y">931</div><div class="kn-l">分裂</div><div class="kn-d">罗波安硬回答<br/>耶罗波安金牛犊</div></div>
    <div class="knail kn-n"><div class="kn-y">722</div><div class="kn-l">北亡</div><div class="kn-d">亚述灭撒玛利亚<br/>十九王无一善终改革</div></div>
    <div class="knail kn-s"><div class="kn-y">586</div><div class="kn-l">南亡</div><div class="kn-d">巴比伦毁殿<br/>大卫灯火似灭未灭</div></div>
    <div class="knail kn-r"><div class="kn-y">538</div><div class="kn-l">归回</div><div class="kn-d">古列下诏<br/>余民与谱系</div></div>
    <div class="knail kn-c"><div class="kn-y">基督</div><div class="kn-l">成全</div><div class="kn-d">真大卫子孙<br/>真圣殿与真国</div></div>
  </div>

  <div class="mnemonic-card card card-gold">
    <h4>口诀（可唱可背）</h4>
    <p class="mnemonic-line"><strong>九三一分家，金牛犊安家；七二二北垮，亚述来扫把；五八六南塌，圣殿变废渣；五三八回家，古列签护照；基督把国拿，影儿变真家。</strong></p>
    <p class="mb-0 muted-note">「分家 / 北垮 / 南塌 / 回家 / 真家」五韵：931 → 722 → 586 → 538 → 基督。</p>
  </div>

  <h4 id="sec-6-united-nodes">联合王国三王速记</h4>
  <div class="table-wrap">
    <table class="data-table">
      <thead><tr><th>王</th><th>约年</th><th>关键</th><th>神学评价</th><th>基督指向</th></tr></thead>
      <tbody>
        <tr><td>扫罗</td><td>约前 1050–1010</td><td>外表高大；擅自献祭；妒大卫</td><td>弃绝：听命胜于献祭</td><td>假受膏对照真受膏</td></tr>
        <tr><td>大卫</td><td>约前 1010–970</td><td>受膏、约柜、拔示巴、大卫之约</td><td>合神心意却非无罪；管教真实</td><td>永远宝座在子孙基督</td></tr>
        <tr><td>所罗门</td><td>约前 970–931</td><td>建殿、智慧、妃嫔偶像</td><td>辉煌下偏邪；埋下分裂种子</td><td>真智慧与真殿是基督</td></tr>
      </tbody>
    </table>
  </div>

  <h4 id="sec-6-reform-kings">南国改革诸王（记忆色）</h4>
  <div class="reform-kings">
    <div class="rk rk-good"><strong>亚撒</strong><span>除偶像起步</span></div>
    <div class="rk rk-good"><strong>约沙法</strong><span>教导律法</span></div>
    <div class="rk rk-mid"><strong>约阿施</strong><span>修殿后偏离</span></div>
    <div class="rk rk-good"><strong>乌西雅</strong><span>强盛却僭越</span></div>
    <div class="rk rk-best"><strong>希西家</strong><span>信靠抗亚述</span></div>
    <div class="rk rk-best"><strong>约西亚</strong><span>发现律法书</span></div>
  </div>
  <p>改革王也不能拦阻最终 586——显明需要<strong>更美之约与完美之王</strong>（耶 31；来 8）。北国自耶罗波安起金牛犊政策，<strong>无一王被评为「行耶和华眼中看为正的事」</strong>。</p>

  <h4 id="sec-6-prophet-sync">先知挂靠年代（对照钉）</h4>
  <div class="mermaid-wrap card">
    <pre class="mermaid">
flowchart TB
  subgraph N["北国线 → 722"]
    N1["耶罗波安金牛犊"] --> N2["亚哈 + 以利亚"]
    N2 --> N3["耶罗波安二世盛世"]
    N3 --> N4["阿摩司 / 何西阿"]
    N4 --> N5["722 亚述"]
  end
  subgraph S["南国线 → 586"]
    S1["罗波安"] --> S2["乌西雅期 · 以赛亚起"]
    S2 --> S3["希西家 · 以赛亚"]
    S3 --> S4["约西亚 · 耶利米起"]
    S4 --> S5["586 巴比伦"]
    S5 --> S6["以西结 / 但以理在被掳地"]
  end
  subgraph R["归回"]
    R1["538 古列"] --> R2["哈该 / 撒迦利亚"]
    R2 --> R3["玛拉基 · 两约间"]
  end
  N5 -.-> S5
  S5 --> R1
  R3 --> C["基督成全"]
  style N5 fill:#5b8fd9,color:#061018
  style S5 fill:#c45c5c,color:#1a0808
  style C fill:#d4af37,color:#1a1200
    </pre>
  </div>

  <div class="essence-block open-essence">
    <h4>诸王精髓：前因 → 后果 → 应用</h4>
    <ul class="essence-list">
      <li><span class="mark-history">前因</span> 求王（撒上8）显不信；所罗门偏邪 + 罗波安愚妄 → 931。</li>
      <li><span class="mark-core">核心</span> 申命记是评分手册：中央敬拜、除偶像、王要抄律法；先知是约的检察官。</li>
      <li><span class="mark-hub">枢纽</span> 大卫之约灯火不灭 → 被掳中仍有谱系 → 基督。</li>
      <li><span class="mark-apply">应用</span> 领袖改革要到根（约西亚）；政治同盟不能替代信靠（以赛亚）；国亡不是故事结束。</li>
      <li><span class="mark-creed">信条</span> 神护理统管帝国（比13）；基督为永恒君王（海德堡 31、50–51）。</li>
    </ul>
  </div>
'''

if 'id="sec-6-dated"' not in html:
    # insert early in kings section after opening paragraph / cards — before color strip or after essence chain
    if 'id="sec-6-color-strip"' in html:
        html = html.replace(
            '<h3 id="sec-6-color-strip">诸王分裂彩色记忆带</h3>',
            KINGS_DATED + '\n  <h3 id="sec-6-color-strip">诸王分裂彩色记忆带</h3>',
            1,
        )
    elif 'id="sec-6-essence-chain"' in html:
        # after essence chain heading block - find next h3 after it
        html = html.replace(
            '<h3 id="sec-6-essence-chain">👑 诸王→被掳→基督：一条因果链</h3>',
            '<h3 id="sec-6-essence-chain">👑 诸王→被掳→基督：一条因果链</h3>',
            1,
        )
        # Insert after first occurrence of color-strip alternative
        idx = html.find('id="sec-6-essence-chain"')
        # find the following h3
        m = re.search(r'<h3 id="sec-6-[^"]+"', html[idx+10:])
        if m:
            pos = idx + 10 + m.start()
            html = html[:pos] + KINGS_DATED + '\n  ' + html[pos:]

# ── Biblical theology expansion before or in sec-4 ──
BT_EXTRA = r'''
  <h3 id="sec-4-angles">多角度读「同一救恩」</h3>
  <div class="angle-grid">
    <div class="angle-card"><span class="ac-ico">🧵</span><strong>圣经神学</strong><p>按救赎历史进展追踪主题：国度、同在、圣殿、安息、余民。</p></div>
    <div class="angle-card"><span class="ac-ico">📜</span><strong>圣约神学</strong><p>行为之约 / 恩典之约；诸分期约是恩典施行，非多套救法。</p></div>
    <div class="angle-card"><span class="ac-ico">📖</span><strong>系统神学</strong><p>从正典综合神论、人论、基督论、救恩论、教会论、终末论。</p></div>
    <div class="angle-card"><span class="ac-ico">⚖️</span><strong>认信神学</strong><p>用信条校准：比、海德堡、多特 + 三大信经条款。</p></div>
    <div class="angle-card"><span class="ac-ico">🗺️</span><strong>历史地理</strong><p>帝国、路线、城邑解释叙事张力与宣教策略。</p></div>
    <div class="angle-card"><span class="ac-ico">❤️</span><strong>生命应用</strong><p>律法显罪、福音安慰、感恩顺服；个人与群体。</p></div>
  </div>

  <h3 id="sec-4-themes">主题追踪简表</h3>
  <div class="table-wrap">
    <table class="data-table">
      <thead><tr><th>主题</th><th>旧约轨迹</th><th>基督成全</th><th>教会/终末</th></tr></thead>
      <tbody>
        <tr><td>神的同在</td><td>园子→会幕→圣殿→荣耀离开</td><td>道成肉身「支搭帐棚」</td><td>圣灵内住；新耶路撒冷有神同在</td></tr>
        <tr><td>国度</td><td>神治→人王→分裂→外邦辖制</td><td>天国近了；十架得国</td><td>已然未济；再来公开</td></tr>
        <tr><td>安息</td><td>创2；安息日；进迦南未全得</td><td>人子是安息日的主</td><td>来4 竭力进入；终末安息</td></tr>
        <tr><td>圣殿/祭</td><td>会幕祭牲；圣殿毁建</td><td>一次永远之祭；身体为殿</td><td>活石建成灵宫；无殿因有羔羊</td></tr>
        <tr><td>余民</td><td>洪水、被掳中保守</td><td>真以色列在基督里</td><td>犹太外邦合一子民</td></tr>
        <tr><td>智慧</td><td>箴/伯/传；敬畏开端</td><td>神的智慧即基督</td><td>十架之道 vs 世界智慧</td></tr>
      </tbody>
    </table>
  </div>

  <div class="mermaid-wrap card">
    <pre class="mermaid">
flowchart TD
  T["圣经神学主线"] --> K["国度：神的王权落实"]
  T --> P["同在：神与子民同住"]
  T --> S["种子/后裔：应许落实"]
  T --> L["土地/产业：安息与继承"]
  K --> C["基督是真大卫王"]
  P --> C2["以马内利 + 圣灵"]
  S --> C3["亚伯拉罕真后裔"]
  L --> C4["在基督里的基业"]
  C --> E["新天新地成全"]
  C2 --> E
  C3 --> E
  C4 --> E
  style T fill:#1a2b45,stroke:#c9a227,color:#ebe6da
  style E fill:#3d9a6a,color:#04140c
    </pre>
  </div>
'''

if 'id="sec-4-angles"' not in html:
    if re.search(r'<h2 id="sec-4"[^>]*>', html):
        # insert after opening of sec-4 — find first h3 after sec-4 or end of first p
        m = re.search(r'<h2 id="sec-4"[^>]*>.*?</h2>\s*<p>.*?</p>', html, re.S)
        if m:
            insert_at = m.end()
            html = html[:insert_at] + '\n' + BT_EXTRA + html[insert_at:]
        else:
            html = html.replace(
                re.search(r'<h2 id="sec-4"[^>]*>.*?</h2>', html).group(0),
                re.search(r'<h2 id="sec-4"[^>]*>.*?</h2>', html).group(0) + '\n' + BT_EXTRA,
                1,
            )

# ── Covenant theology small deepen ──
COV_EXTRA = r'''
  <h3 id="sec-3-why">为何必须用圣约框架？</h3>
  <div class="card-grid cols-2">
    <div class="card">
      <span class="card-tag">前因</span>
      <p class="mb-0">人不是抽象「宗教动物」，乃是<strong>约下的受造者</strong>：在亚当里有法律代表；在基督里有恩典代表（罗5；林前15）。离开圣约，称义易变成道德主义或神秘主观。</p>
    </div>
    <div class="card">
      <span class="card-tag mark-creed">信条</span>
      <p class="mb-0">海德堡 Q&amp;A 9–18 说明人亏欠与中保必须是真神真人；比利时 22–23 讲归算之义；多特强调拣选与坚忍——皆假设圣约代表结构。</p>
    </div>
  </div>
'''

if 'id="sec-3-why"' not in html:
    if 'id="sec-3-1"' in html:
        html = html.replace(
            '<h3 id="sec-3-1">两大总约</h3>',
            COV_EXTRA + '\n  <h3 id="sec-3-1">两大总约</h3>',
            1,
        )

# ── Creeds cite expansion small ──
CREED_EXTRA = r'''
  <h3 id="sec-8-cite">条款速引（勿替代正式译本）</h3>
  <div class="table-wrap">
    <table class="data-table">
      <thead><tr><th>文献</th><th>常引条款</th><th>护卫主题</th></tr></thead>
      <tbody>
        <tr><td>使徒信经</td><td>全文结构</td><td>三一、教会、赦罪、复活、永生</td></tr>
        <tr><td>尼西亚信经</td><td>「与父一体」等</td><td>基督真神；圣灵是主赐生命者</td></tr>
        <tr><td>亚他那修信经</td><td>三一/二性段落</td><td>拒模态与混性</td></tr>
        <tr><td>比利时信条</td><td>2–7 圣经；16 拣选；21–23 中保与称义；27–35 教会圣礼</td><td>权威、救恩、教会</td></tr>
        <tr><td>海德堡要理</td><td>Q1；Q2–3；Q12–23；Q31；Q65–85；Q86–129</td><td>安慰、罪/救/感恩、圣礼、十诫主祷文</td></tr>
        <tr><td>多特信经</td><td>第一–五项</td><td>拣选、救赎、败坏、恩典、坚忍</td></tr>
      </tbody>
    </table>
  </div>
  <p class="muted-note">本站只标条款号与要旨，<strong>不粘贴信条全文</strong>；研读请对照教会正式中文译本。</p>
'''

if 'id="sec-8-cite"' not in html:
    if 'id="sec-8-essence"' in html:
        html = html.replace(
            '<h3 id="sec-8-essence">信条校准精髓</h3>',
            CREED_EXTRA + '\n  <h3 id="sec-8-essence">信条校准精髓</h3>',
            1,
        )
    elif 'id="sec-8"' in html:
        m = re.search(r'<h2 id="sec-8"[^>]*>.*?</h2>', html)
        if m:
            html = html[:m.end()] + '\n' + CREED_EXTRA + html[m.end():]

# ── Footer version note ──
html = html.replace(
    "Soli Deo Gloria",
    "Soli Deo Gloria · v2 · 2026-09-30",
    1,
)

# Fix storyline insertion if it broke section tags - ensure sec-0 still in a section
# Check for accidental double <section
# Also fix if STORYLINE was inserted with wrong fallback creating unclosed tags
if html.count('<section') != html.count('</section>'):
    # try to balance by not using broken fallback - read was already done
    pass

# ── CSS additions ──
CSS_ADD = r'''

/* ===== v2 additions: storyline, geo, dated nodes, kings nails, dynamics ===== */
.ver-badge {
  display: inline-block;
  margin-left: .35rem;
  padding: .12rem .55rem;
  font-size: .55em;
  vertical-align: middle;
  border-radius: var(--radius-pill);
  background: linear-gradient(135deg, rgba(212,175,55,.35), rgba(107,163,224,.25));
  border: 1px solid rgba(212,175,55,.55);
  color: var(--gold-light);
  font-weight: 800;
  letter-spacing: .06em;
  animation: badge-pulse 3.2s ease-in-out infinite;
}
@keyframes badge-pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(212,175,55,.25); }
  50% { box-shadow: 0 0 16px 2px rgba(212,175,55,.35); }
}
@media (prefers-reduced-motion: reduce) {
  .ver-badge { animation: none; }
}

.storyline-flow {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 6px;
  margin: 1rem 0 1.25rem;
  padding: 8px 0;
}
.sl-act {
  flex: 1 1 72px;
  min-width: 72px;
  max-width: 110px;
  padding: 10px 8px;
  border-radius: 12px;
  border: 1px solid rgba(212,175,55,.28);
  background: rgba(16,28,48,.9);
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 4px;
  transition: transform .25s ease, box-shadow .25s ease, border-color .25s;
}
.sl-act:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-glow);
  border-color: rgba(212,175,55,.55);
}
.sl-n {
  display: inline-flex;
  align-self: center;
  width: 22px; height: 22px;
  align-items: center; justify-content: center;
  border-radius: 50%;
  font-size: .72rem;
  font-weight: 800;
  background: rgba(212,175,55,.2);
  color: var(--gold-light);
}
.sl-act strong { font-size: .88rem; color: var(--text); }
.sl-act small { font-size: .68rem; color: var(--text-muted); line-height: 1.3; }
.sl-arrow {
  display: flex; align-items: center;
  color: var(--gold); opacity: .7; font-weight: 700;
  flex: 0 0 auto;
}
.sl-create { border-color: rgba(212,175,55,.45); }
.sl-fall { border-color: rgba(196,92,92,.45); }
.sl-promise { border-color: rgba(94,196,192,.45); }
.sl-israel { border-color: rgba(232,168,92,.45); }
.sl-exile { border-color: rgba(196,92,92,.5); background: rgba(196,92,92,.08); }
.sl-return { border-color: rgba(61,154,106,.45); }
.sl-christ { border-color: rgba(179,157,219,.55); background: rgba(179,157,219,.1); }
.sl-end { border-color: rgba(61,154,106,.5); background: rgba(61,154,106,.1); }
@media (max-width: 700px) {
  .sl-arrow { display: none; }
  .sl-act { flex: 1 1 40%; max-width: none; }
}

.dated-nodes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 8px;
  margin: .75rem 0 1.25rem;
}
.dn {
  padding: 10px 12px;
  border-radius: 12px;
  border: 1px solid rgba(212,175,55,.28);
  background: rgba(16,28,48,.88);
  display: flex;
  flex-direction: column;
  gap: 3px;
  min-height: 92px;
  transition: transform .2s ease, border-color .2s;
}
.dn:hover { transform: translateY(-2px); border-color: rgba(212,175,55,.5); }
.dn-y { font-family: var(--font-mono); font-size: .72rem; font-weight: 800; color: var(--gold-light); letter-spacing: .03em; }
.dn-t { font-weight: 700; font-size: .9rem; color: var(--text); line-height: 1.25; }
.dn-n { font-size: .75rem; color: var(--text-muted); line-height: 1.35; }
.dn-gold { border-color: rgba(212,175,55,.4); }
.dn-split { border-color: rgba(232,168,92,.5); background: rgba(232,168,92,.08); }
.dn-north { border-color: rgba(91,143,217,.5); background: rgba(91,143,217,.1); }
.dn-south { border-color: rgba(196,92,92,.5); background: rgba(196,92,92,.1); }
.dn-return { border-color: rgba(61,154,106,.45); background: rgba(61,154,106,.08); }
.dn-silence { border-color: rgba(123,159,224,.4); }
.dn-christ { border-color: rgba(240,216,120,.65); background: rgba(240,216,120,.12); }
.dn-church { border-color: rgba(74,144,217,.45); }
.dn-end { border-color: rgba(61,154,106,.55); }

.empire-strip {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: .75rem 0 1.1rem;
}
.emp {
  flex: 1 1 100px;
  padding: 12px 10px;
  border-radius: 12px;
  text-align: center;
  border: 1px solid transparent;
  display: flex;
  flex-direction: column;
  gap: 4px;
  transition: transform .22s ease, filter .22s;
}
.emp:hover { transform: scale(1.03); filter: brightness(1.08); }
.emp strong { font-size: .95rem; }
.emp span { font-size: .75rem; opacity: .9; line-height: 1.3; }
.emp-eg { background: rgba(201,162,39,.18); border-color: rgba(201,162,39,.4); color: #f0d878; }
.emp-as { background: rgba(91,143,217,.18); border-color: rgba(91,143,217,.4); color: #b8d4f0; }
.emp-bb { background: rgba(196,92,92,.18); border-color: rgba(196,92,92,.4); color: #f0b8b8; }
.emp-pe { background: rgba(61,154,106,.18); border-color: rgba(61,154,106,.4); color: #a8dfc4; }
.emp-gr { background: rgba(123,159,224,.16); border-color: rgba(123,159,224,.4); color: #b8c8f0; }
.emp-rm { background: rgba(179,157,219,.16); border-color: rgba(179,157,219,.4); color: #d4c4f0; }

.kings-nail-row {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 8px;
  margin: 1rem 0;
}
@media (max-width: 800px) {
  .kings-nail-row { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 420px) {
  .kings-nail-row { grid-template-columns: 1fr; }
}
.knail {
  padding: 14px 12px;
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,.08);
  text-align: center;
  transition: transform .25s ease, box-shadow .25s;
  box-shadow: var(--shadow-soft);
}
.knail:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-glow);
}
.kn-y {
  font-family: var(--font-mono);
  font-size: 1.35rem;
  font-weight: 800;
  letter-spacing: .04em;
  line-height: 1.1;
}
.kn-l { font-weight: 750; font-size: 1rem; margin: 4px 0; }
.kn-d { font-size: .75rem; opacity: .9; line-height: 1.35; }
.kn-split { background: rgba(232,168,92,.16); border-color: rgba(232,168,92,.45); color: #f0d0a0; }
.kn-n { background: rgba(91,143,217,.16); border-color: rgba(91,143,217,.45); color: #b8d4f0; }
.kn-s { background: rgba(196,92,92,.16); border-color: rgba(196,92,92,.45); color: #f0b8b8; }
.kn-r { background: rgba(61,154,106,.16); border-color: rgba(61,154,106,.45); color: #a8dfc4; }
.kn-c { background: rgba(212,175,55,.2); border-color: rgba(212,175,55,.55); color: #f0d878; }

.mnemonic-card { margin: 1rem 0 1.25rem; }
.mnemonic-line {
  font-size: 1.02rem;
  line-height: 1.7;
  color: var(--gold-light);
}
.muted-note { color: var(--text-muted); font-size: .86rem; }

.reform-kings {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: .75rem 0 1rem;
}
.rk {
  flex: 1 1 100px;
  padding: 10px 12px;
  border-radius: 10px;
  border: 1px solid rgba(61,154,106,.35);
  background: rgba(61,154,106,.1);
  display: flex;
  flex-direction: column;
  gap: 2px;
  transition: background .2s, transform .2s;
}
.rk:hover { transform: translateY(-2px); }
.rk strong { color: #a8dfc4; font-size: .92rem; }
.rk span { font-size: .75rem; color: var(--text-muted); }
.rk-best { border-color: rgba(212,175,55,.5); background: rgba(212,175,55,.12); }
.rk-best strong { color: var(--gold-light); }
.rk-mid { border-color: rgba(232,168,92,.4); background: rgba(232,168,92,.1); }
.rk-mid strong { color: #f0d0a0; }
.rk-good strong { color: #a8dfc4; }

.angle-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 10px;
  margin: .85rem 0 1.25rem;
}
.angle-card {
  padding: 14px 12px;
  border-radius: 12px;
  border: 1px solid rgba(74,100,140,.35);
  background: rgba(16,28,48,.85);
  transition: border-color .25s, transform .25s, box-shadow .25s;
}
.angle-card:hover {
  border-color: rgba(212,175,55,.45);
  transform: translateY(-3px);
  box-shadow: var(--shadow-glow-soft);
}
.ac-ico { font-size: 1.2rem; display: block; margin-bottom: 4px; }
.angle-card strong { display: block; color: var(--gold-light); margin-bottom: 4px; font-size: .92rem; }
.angle-card p { margin: 0; font-size: .8rem; color: var(--text-muted); line-height: 1.45; }

.map-card { overflow: hidden; padding: 8px; }
.geo-svg { border-radius: 10px; }
.geo-table td:first-child { font-weight: 700; color: var(--gold-light); white-space: nowrap; }

/* Smooth section reveal feel */
.mod-storyline, .mod-geo, .mod-kings, .mod-quicklearn, .mod-covenant, .mod-bt {
  transition: opacity .35s ease;
}
.card, .knail, .dn, .sl-act, .emp, .angle-card, .kms-item, .vt-item {
  will-change: transform;
}

/* Ensure mermaid + tables don't overflow on phone */
.mermaid-wrap {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  max-width: 100%;
}
.mermaid-wrap .mermaid { min-width: min(100%, 280px); }
.table-wrap {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  max-width: 100%;
  margin-bottom: 1rem;
}

/* Preserve body-level sidebar stacking — do not nest TOC inside app-shell */
/* (v1 fix retained: .sidebar position:fixed; z-index 1000; body.nav-open rules) */
'''

if "v2 additions: storyline" not in css:
    css += CSS_ADD

# ── package.json ──
PKG.write_text("""{
  "name": "reformed-bible-study-continental-20260930-v2",
  "version": "2.0.0",
  "private": true,
  "description": "欧陆改革宗整本圣经研读站点 v2（2026-09-30）：时间线·地理·圣约·诸王纪年·66卷速学",
  "scripts": {
    "start": "npx --yes serve -l 3456 .",
    "preview": "npx --yes serve -l 3456 ."
  },
  "keywords": ["bible", "reformed", "zh-CN", "static", "continental"],
  "homepage": "https://reformed-bible-study-continental-20260930-v2.surge.sh/"
}
""", encoding="utf-8")

# Validate HTML section balance / storyline placement
sec_open = html.count("<section")
sec_close = html.count("</section>")
print("sections open/close:", sec_open, sec_close)

# Check critical ids
for i in ["sec-storyline", "sec-geo", "sec-6-dated", "sec-2-dated-nodes", "sec-4-angles", "sec-3-why", "sec-8-cite"]:
    print(i, "OK" if f'id="{i}"' in html else "MISSING")

# Fix storyline if inserted incorrectly duplicating section open on sec-0
# Detect pattern: STORYLINE then <section ... sec-0 duplicated
if html.count('id="s0"') > 1 or html.count('id="sec-0"') > 1:
    print("WARN duplicate sec-0")

# If storyline fallback created: STORYLINE + <section class="mod-intro" without closing previous
# Check whether <!-- ========== 0 导论 ========== --> exists
print("has intro comment", "<!-- ========== 0 导论 ========== -->" in html or "导论：如何读" in html)

HTML.write_text(html, encoding="utf-8")
CSS.write_text(css, encoding="utf-8")
print("Wrote HTML", HTML.stat().st_size, "CSS", CSS.stat().st_size)
