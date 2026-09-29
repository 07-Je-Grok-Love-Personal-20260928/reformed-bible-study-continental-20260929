# 欧陆改革宗 · 整本圣经研读

静态 HTML 教学网站：以**三项联合信条**（比利时信条、海德堡要理问答、多特信经）与**三大普世信经**（使徒、尼西亚、亚他那修）为认信框架，贯通救赎历史、圣约神学、圣经神学主线、诸王时代与整本分卷要点。

## 特色

- 单页应用式结构：可折叠左侧目录、粘性顶栏、阅读进度条、平滑锚点滚动
- 深色海军 / 金色主题，移动优先自适应
- Mermaid 流程图 / 思维导图（CDN）；内联 SVG 示意地图
- 诸王年表、圣约对照、正典与救赎历史表、记忆口诀卡
- 分卷「背景·目的·提纲·神学·基督·应用」六栏折叠阅读
- 除 Mermaid CDN 外，资源可本地打开（离线可用样式与脚本）

## 目录结构

```
bible-study-reformed/
├── index.html          # 主页面（全部内容）
├── assets/
│   ├── styles.css      # 主题与布局
│   └── app.js          # 目录、侧栏、进度、Mermaid 初始化
├── package.json        # 可选本地预览脚本
└── README.md
```

## 本地预览

### 方式一：直接打开

用浏览器打开 `index.html`。若 Mermaid 图表因 `file://` 策略未渲染，请改用本地服务器。

### 方式二：npm 脚本

```bash
cd bible-study-reformed
npm install   # 安装 serve（可选）
npm start     # 默认 http://localhost:3456
```

### 方式三：任意静态服务器

```bash
python3 -m http.server 3456
# 或 npx serve -l 3456
```

## 部署说明（占位）

可将本目录原样部署到任意静态托管：

- GitHub Pages / Cloudflare Pages / Netlify / Vercel（静态导出）
- Nginx / Caddy 指向本目录为 `root`
- 无需后端；确保 `assets/` 路径相对正确

部署检查清单：

1. `index.html` 为入口
2. CDN 可访问 `cdn.jsdelivr.net`（Mermaid），或改为自托管 mermaid
3. 字符编码 UTF-8

## 认信立场

唯独圣经、唯独恩典、唯独信心、唯独基督、唯独荣耀归于神。以基督为中心的文法—历史释经；拒自由派否定超自然，亦拒不顾作者原意的随意寓意。信条引用仅标条款号，请对照正式译本全文。

## 许可与使用

教学与教会内部学习使用。圣经经文请使用您已获授权的译本。年代数字多为教学常用概数。

Soli Deo Gloria

## 在线地址

- GitHub 仓库：https://github.com/07-Je-Grok-Love-Personal-20260928/bible-study-reformed
- GitHub Pages：https://07-je-grok-love-personal-20260928.github.io/bible-study-reformed/
- Surge：https://reformed-bible-study.surge.sh/
- Netlify：部署完成后补充

