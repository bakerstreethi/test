# HOO TRAVEL · 花火出国游 品牌资料

**云端文件固定存放位置（Google Drive）**：https://drive.google.com/drive/folders/1NTASyyIuE3MG1hyTh0EZtU_gkehUBtDu
以后新文件都放这个文件夹。

品牌紫 `#5237A0`，夜紫 `#261A55`，荧光黄绿 `#D8F36A`（只做点缀）。

## 文件夹

| 路径 | 内容 |
|---|---|
| `logo/final/` | **正式 logo**，SVG 是矢量原稿，`png/` 里是各种尺寸 |
| `logo/avatar/` | **圆形头像**，夜紫、品牌紫、雾紫三种底色，每种有方形（平台自己裁圆）和已裁成圆形（透明角）两种 |
| `logo/archive/` | 早期被淘汰的草稿，仅留作记录，不要使用 |
| `brand/DESIGN.md` | 网站设计规范（颜色、字体、间距、组件） |
| `brand/tokens.css` | 与规范对应的颜色、字体、间距变量 |
| `brand/colors.css` · `colors.json` | 品牌色板 |
| `brand-guide/index.html` | **品牌指南**，单文件，logo、头像、色彩、字体、下载中心都在里面，可直接放进网站后台 |
| `brand-guide/build.py` | 重新生成品牌指南：改完 `template.html` 或 `build.py` 后运行 `python3 brand-guide/build.py` |
| `brand/archive/` | 旧版色彩说明书，已被品牌指南取代 |
| `brand/web-directions/` | 三个首页方向的效果图 |
| `site/index.html` | 新首页，单文件，图片已内联，直接用浏览器打开 |
| `site/index.src.html` · `build.py` · `img/` | 首页源文件。改完运行 `python3 site/build.py` 重新生成 `index.html` |

## Logo 用在哪里

| 场景 | 文件 |
|---|---|
| 网站页头、PPT、宣传册（浅色底） | `logo/final/hoo-logo-horizontal-light.svg` |
| 网站页头、视频片尾（深色或紫色底） | `logo/final/hoo-logo-horizontal-dark.svg` |
| 近似方形的位置（竖版） | `logo/final/hoo-logo-stacked-light.svg` / `-dark.svg` |
| 微信、小红书、Instagram 头像 | `logo/final/png/hoo-avatar-800.png` |
| iOS 主屏图标 | `logo/final/png/hoo-icon-app-180.png` |
| App 图标 | `logo/final/png/hoo-icon-app-1024.png` |
| 网站 favicon | `logo/final/favicon.ico` 和 `hoo-favicon.svg` |
| 只要图标，不要字标 | `logo/final/hoo-icon-light.svg` / `-dark.svg` |

16px 的 favicon 去掉了圆环缺口处的三道火花线，小尺寸下更清楚。

## 注意

- 字标（`HOOTRAVEL` 的字形）沿用品牌原有的版本，只改了颜色：HOO 与圆环是品牌紫，TRAVEL 是灰紫 `#6F6A8E`。
- 首页里的价格和文案取自线上网站 hootravel.com 的当时内容，上线前请核对。
- 首页里指向 `www.hootravel.com` 的链接是临时地址，换成新站后需要改。
