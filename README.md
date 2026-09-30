# 欧陆改革宗 · 整本圣经研读

静态 HTML 教学网站：以**三项联合信条**（比利时信条、海德堡要理问答、多特信经）与**三大普世信经**（使徒、尼西亚、亚他那修）为认信框架，贯通救赎历史、圣约神学、圣经神学主线、诸王时代与整本分卷要点。

**内容版本：v2.2**（工作树回滚至 `5bae235` 的 66卷速学 + 时间线/地图可视化；仅从新近版本保留「故事线思维导图（Mermaid）」一节）

## 特色

- 单页应用式结构：可折叠左侧目录、粘性顶栏、阅读进度条、平滑锚点滚动
- 深色海军 / 金色主题，移动优先自适应；**body 级固定 TOC**（手机不重叠）
- Mermaid 流程图 / 思维导图（CDN，标签用 `<br/>`）；含诸王示意地图与被掳路线等既有可视化（`5bae235` 基线）
- 诸王年表、圣约对照、正典与救赎历史表、记忆口诀卡
- 分卷「背景·目的·提纲·神学·基督·应用」六栏折叠阅读
- **66卷速学掌握**：一书一句话、背景、骨架、主题、基督指向、记忆钩、应用
- **故事线思维导图（Mermaid）**：在「一条线」之后保留思维导图（标签用 `<br/>`）；CSS/JS 强制奶油节点、深色字、金色边（mindmap 忽略 flowchart themeVariables）；未并入已否决的八幕流程、地理专章、诸王五钉等 v2 块

## 目录结构

```
reformed-bible-study-continental-20260929/
├── index.html          # 主页面（全部内容）
├── assets/
│   ├── styles.css      # 主题与布局
│   └── app.js          # 目录、侧栏、进度、Mermaid 初始化
├── package.json
└── README.md
```

## 本地预览

```bash
cd reformed-bible-study-continental-20260929
npm start     # 默认 http://localhost:3456
# 或 python3 -m http.server 3456
```

## 认信立场

唯独圣经、唯独恩典、唯独信心、唯独基督、唯独荣耀归于神。以基督为中心的文法—历史释经；拒自由派否定超自然，亦拒不顾作者原意的随意寓意。信条引用仅标条款号，请对照正式译本全文。年代数字多为教学常用概数。

Soli Deo Gloria

## 在线地址

- GitHub 仓库：https://github.com/07-Je-Grok-Love-Personal-20260928/reformed-bible-study-continental-20260929
- GitHub Pages：https://07-je-grok-love-personal-20260928.github.io/reformed-bible-study-continental-20260929/
- Surge：https://reformed-bible-study-20260929.surge.sh/
- Netlify：https://reformed-bible-study-continental-20260929.netlify.app/
