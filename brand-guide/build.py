"""生成 brand-guide/index.html：把 template.html 里的占位符替换成数据和内嵌资源。
用法：python3 brand-guide/build.py
"""
import base64, html, json, pathlib

here = pathlib.Path(__file__).parent
root = here.parent
logo = root / "logo" / "final"
avatar = root / "logo" / "avatar"
brand = root / "brand"


def b64(p: pathlib.Path) -> str:
    return base64.b64encode(p.read_bytes()).decode()


def uri(p: pathlib.Path, mime: str) -> str:
    return f"data:{mime};base64,{b64(p)}"


# ---------- 颜色 ----------
core = [
    ("夜紫 Night", "#261A55", "页面主底色、标题", "#F3F0FA"),
    ("品牌紫 Purple", "#5237A0", "Logo、主按钮、链接", "#FFFFFF"),
    ("亮紫 Bright", "#7D63C8", "深底上的装饰，不放文字", "#FFFFFF"),
    ("浅紫 Lavender", "#D9D0F4", "深底上的次级文字", "#261A55"),
    ("雾紫 Mist", "#F3F0FA", "深底上的主文字、App 底色", "#261A55"),
    ("纸白 Paper", "#F7F6FB", "浅色区块的底色", "#261A55"),
    ("沙色 Sand", "#E8D9C5", "照片上的字、高端度假的暖色", "#261A55"),
    ("荧光 Lime", "#D8F36A", "信号色，每屏一处", "#261A55"),
    ("灰紫 Slate", "#6F6A8E", "次级文字、TRAVEL 字标", "#FFFFFF"),
]
scale = [
    ("夜紫 950", "#170F3A", "页脚、最深的底", "#F3F0FA"),
    ("夜紫 800", "#2F2266", "深底上的卡片、输入框", "#F3F0FA"),
    ("夜紫 700", "#3B2F78", "深底上的分割线", "#F3F0FA"),
    ("深底说明字", "#B4ABDD", "深底上的说明文字", "#261A55"),
    ("雾紫 2", "#EEEBF6", "浅色区块的第二层", "#261A55"),
    ("浅底分割线", "#E1DCEF", "浅底上的分割线", "#261A55"),
]


def rgb(h):
    h = h.lstrip("#")
    return ", ".join(str(int(h[i:i + 2], 16)) for i in (0, 2, 4))


def swatch(n, h, role, fg):
    return (f'<button class="hg-sw" type="button" data-copy="{h}" aria-label="复制 {n} {h}">'
            f'<span class="c" style="background:{h};color:{fg}">{h}</span>'
            f'<span class="m"><b>{n}</b><span>{role}</span><code>RGB {rgb(h)}</code></span></button>')


CORE = "".join(swatch(*c) for c in core)
SCALE = "".join(swatch(*c) for c in scale)

lines = [
    ("英伦乡村 · 慢游 · 深度", "", "天气：黄昏时回到壁炉边的暖光。安静，留白多，靠摄影说话。",
     [("夜紫", "#261A55"), ("纸白", "#F7F6FB"), ("品牌紫", "#5237A0"), ("荧光", "#D8F36A"), ("蜂蜜石", "#D9B88B"), ("苔绿", "#55704F")],
     "荧光最克制，一个词或一个小标记。"),
    ("北欧 · 冬季 · 活力半自助", "", "天气：极夜加极光。深底大面积，最亮、最冷、最有精神。",
     [("夜紫", "#261A55"), ("品牌紫", "#5237A0"), ("亮紫", "#7D63C8"), ("荧光", "#D8F36A"), ("冰蓝", "#BFE2F5"), ("极光青", "#5ED9BC")],
     "荧光可以放大用，约 12%，做标题关键词和极光渐变。"),
    ("英伦度假 · 高端定制", "建议", "天气：深夜壁炉边。更暗、更静，用沙色代替荧光。",
     [("夜紫", "#261A55"), ("茄紫", "#3B2457"), ("品牌紫", "#5237A0"), ("纸白", "#F7F6FB"), ("沙色", "#E8D9C5")],
     "不使用荧光（logo 里的小圆除外）。"),
    ("欧洲线路", "筹备中", "天气：午后的阳光。线路定下来之前先占位，可以调整。",
     [("夜紫", "#261A55"), ("品牌紫", "#5237A0"), ("纸白", "#F7F6FB"), ("荧光", "#D8F36A"), ("杏色", "#F6D8C2"), ("赤陶", "#D8825C")],
     "荧光小点缀，不超过 3%；不与赤陶同时大面积出现。"),
]


def line_card(t, draft, d, chips, rule):
    dr = f'<span class="hg-draft">{draft}</span>' if draft else ""
    ch = "".join(f'<span><i style="background:{h}"></i>{n} {h}</span>' for n, h in chips)
    return f'<div class="hg-card hg-line"><h4>{t}{dr}</h4><p>{d}</p><div class="hg-chips">{ch}</div><p>{rule}</p></div>'


LINES = "".join(line_card(*l) for l in lines)

names = {"#FAF7F2": "奶油", "#261A55": "夜紫", "#5237A0": "品牌紫", "#D9B88B": "蜂蜜石", "#55704F": "苔绿", "#D8F36A": "荧光",
         "#BFE2F5": "冰蓝", "#5ED9BC": "极光青", "#F6D8C2": "杏色", "#D8825C": "赤陶", "#3B2457": "茄紫", "#E8D9C5": "沙色", "#F7F6FB": "纸白"}
names.pop("#FAF7F2")
bars = {
    "英伦乡村": [("#261A55", 38), ("#F7F6FB", 28), ("#5237A0", 16), ("#D9B88B", 10), ("#55704F", 6), ("#D8F36A", 2)],
    "北欧冬季": [("#261A55", 50), ("#5237A0", 14), ("#BFE2F5", 12), ("#5ED9BC", 8), ("#D8F36A", 12), ("#F7F6FB", 4)],
    "英伦度假": [("#3B2457", 40), ("#261A55", 22), ("#E8D9C5", 22), ("#F7F6FB", 8), ("#5237A0", 8)],
    "欧洲（筹备中）": [("#F7F6FB", 30), ("#F6D8C2", 20), ("#261A55", 17), ("#5237A0", 17), ("#D8825C", 13), ("#D8F36A", 3)],
}
BARS = "".join(
    f'<div class="hg-brow"><span>{k}</span><div class="hg-bar">' +
    "".join(f'<i style="width:{w}%;background:{c}" title="{names[c]} {w}%"></i>' for c, w in v) + "</div></div>"
    for k, v in bars.items())
LEG = "".join(f'<span><i style="background:{h}"></i>{n}</span>' for h, n in names.items())

rows = [
    ("#5237A0", "#F7F6FB", "品牌紫字 / 纸白底", "8.14", "y"), ("#261A55", "#D8F36A", "夜紫字 / 荧光底", "12.45", "y"),
    ("#D8F36A", "#261A55", "荧光字 / 夜紫底", "12.45", "y"), ("#D8F36A", "#5237A0", "荧光字 / 品牌紫底", "7.02", "y"),
    ("#D9D0F4", "#261A55", "浅紫字 / 夜紫底", "10.49", "y"), ("#B4ABDD", "#261A55", "说明字 / 夜紫底", "7.21", "y"),
    ("#6F6A8E", "#F7F6FB", "灰紫字 / 纸白底", "4.73", "y"), ("#E8D9C5", "#3B2457", "沙色字 / 茄紫底", "9.62", "y"),
    ("#261A55", "#5ED9BC", "夜紫字 / 极光青底", "8.91", "y"), ("#261A55", "#D8825C", "夜紫字 / 赤陶底", "5.34", "y"),
    ("#7D63C8", "#261A55", "亮紫字 / 夜紫底", "3.30", "n"), ("#D8825C", "#F7F6FB", "赤陶字 / 纸白底", "2.7", "n"),
    ("#D8F36A", "#F7F6FB", "荧光字 / 纸白底", "1.2", "n"),
]
TBL = "".join(
    f'<div class="hg-row"><div class="s" style="background:{b};color:{f}">Aa</div><div class="r">{r}</div><div>{t}</div>'
    f'<div class="v {v}">{"通过" if v == "y" else "避免"}</div></div>' for f, b, t, r, v in rows)

# ---------- 下载 ----------
MIME = {".svg": "image/svg+xml", ".png": "image/png", ".ico": "image/x-icon", ".css": "text/css",
        ".json": "application/json", ".md": "text/markdown"}


def act(label, p: pathlib.Path):
    return f'<a class="hg-btn sm" href="{uri(p, MIME[p.suffix])}" download="{p.name}">{label}</a>'


P = logo / "png"
groups = [
    ("完整 Logo（图标 + 字标）", [
        ("横版 · 浅底（紫色版）", "网页页头、PPT、宣传册", [("SVG", logo / "hoo-logo-horizontal-light.svg"), ("PNG 1200", P / "hoo-logo-horizontal-light-1200w.png"), ("PNG 3000", P / "hoo-logo-horizontal-light-3000w.png")]),
        ("横版 · 深底（浅色版）", "深色或紫色背景、视频片尾", [("SVG", logo / "hoo-logo-horizontal-dark.svg"), ("PNG 1200", P / "hoo-logo-horizontal-dark-1200w.png"), ("PNG 3000", P / "hoo-logo-horizontal-dark-3000w.png")]),
        ("竖版 · 浅底", "近似方形的位置", [("SVG", logo / "hoo-logo-stacked-light.svg"), ("PNG 2000", P / "hoo-logo-stacked-light-2000w.png")]),
        ("竖版 · 深底", "近似方形的深色位置", [("SVG", logo / "hoo-logo-stacked-dark.svg"), ("PNG 2000", P / "hoo-logo-stacked-dark-2000w.png")]),
    ]),
    ("图标与网站图标", [
        ("图标 · 浅底（透明背景）", "只需要图标、不要字标", [("SVG", logo / "hoo-icon-light.svg"), ("PNG 1024", P / "hoo-icon-light-1024.png")]),
        ("图标 · 深底（透明背景）", "深色背景上的图标", [("SVG", logo / "hoo-icon-dark.svg"), ("PNG 1024", P / "hoo-icon-dark-1024.png")]),
        ("App 图标（圆角方形）", "iOS / 安卓 App，不要再自己加圆角", [("SVG", logo / "hoo-icon-app.svg"), ("PNG 1024", P / "hoo-icon-app-1024.png"), ("PNG 180", P / "hoo-icon-app-180.png")]),
        ("网站图标 favicon", "浏览器标签页，16px 版本已去掉火花线", [("ICO", logo / "favicon.ico"), ("SVG", logo / "hoo-favicon.svg"), ("PNG 32", P / "favicon-32.png"), ("PNG 16", P / "favicon-16.png")]),
    ]),
    ("头像", [
        ("夜紫底 · 方形满铺（默认）", "上传到微信、小红书、Instagram", [("PNG 1024", avatar / "hoo-avatar-night-1024.png"), ("SVG", avatar / "hoo-avatar-night.svg")]),
        ("夜紫底 · 已裁成圆形", "放进文档、网页、海报（四角透明）", [("PNG 1024", avatar / "hoo-avatar-night-circle-1024.png"), ("SVG", avatar / "hoo-avatar-night-circle.svg")]),
        ("品牌紫底 · 方形满铺", "需要更醒目的场合", [("PNG 1024", avatar / "hoo-avatar-purple-1024.png"), ("SVG", avatar / "hoo-avatar-purple.svg")]),
        ("品牌紫底 · 已裁成圆形", "同上，已裁圆", [("PNG 1024", avatar / "hoo-avatar-purple-circle-1024.png"), ("SVG", avatar / "hoo-avatar-purple-circle.svg")]),
        ("雾紫浅底（备选）· 方形 / 圆形", "浅色界面里使用，对比较弱", [("方形 PNG", avatar / "hoo-avatar-mist-1024.png"), ("圆形 PNG", avatar / "hoo-avatar-mist-circle-1024.png")]),
    ]),
]
DOWNLOADS = ""
for gt, items in groups:
    lis = "".join(f'<li><span class="n">{n}</span><span class="u">{u}</span><span class="acts">{"".join(act(l, p) for l, p in fs)}</span></li>' for n, u, fs in items)
    DOWNLOADS += f'<div class="hg-dl"><h3>{gt}</h3><ul>{lis}</ul></div>'

# 颜色变量文件（由本脚本统一生成，保证和页面一致）
tok = {"core": {"night": "#261A55", "purple": "#5237A0", "bright": "#7D63C8", "lavender": "#D9D0F4", "mist": "#F3F0FA", "paper": "#F7F6FB",
                "sand": "#E8D9C5", "lime": "#D8F36A", "slate": "#6F6A8E"},
       "scale": {"night-950": "#170F3A", "night-800": "#2F2266", "night-700": "#3B2F78", "text-on-night-muted": "#B4ABDD", "mist-2": "#EEEBF6", "line-on-paper": "#E1DCEF"},
       "lines": {"uk": {"honey": "#D9B88B", "moss": "#55704F"}, "nordic": {"ice": "#BFE2F5", "aurora": "#5ED9BC"},
                 "retreat_draft": {"aubergine": "#3B2457"}, "europe_draft": {"apricot": "#F6D8C2", "terracotta": "#D8825C"}}}
(brand / "colors.json").write_text(json.dumps(tok, indent=2, ensure_ascii=False), encoding="utf-8")
flat = {**tok["core"], **tok["scale"], **{k: v for g in tok["lines"].values() for k, v in g.items()}}
(brand / "colors.css").write_text(":root{\n" + "".join(f"  --hoo-{k}: {v};\n" for k, v in flat.items()) + "}\n", encoding="utf-8")
tokens_css = (brand / "tokens.css").read_text(encoding="utf-8")

DOWNLOADS += ('<div class="hg-dl"><h3>色彩与规范文件</h3><ul>'
              f'<li><span class="n">tokens.css</span><span class="u">网页开发用：颜色、字体、间距、圆角的完整变量</span><span class="acts">{act("下载", brand / "tokens.css")}</span></li>'
              f'<li><span class="n">colors.css</span><span class="u">只含颜色的 CSS 变量</span><span class="acts">{act("下载", brand / "colors.css")}</span></li>'
              f'<li><span class="n">colors.json</span><span class="u">颜色的 JSON 版本，给程序读取</span><span class="acts">{act("下载", brand / "colors.json")}</span></li>'
              f'<li><span class="n">DESIGN.md</span><span class="u">网站设计规范全文（颜色、字体、间距、组件）</span><span class="acts">{act("下载", brand / "DESIGN.md")}</span></li>'
              '</ul></div>')

rep = {
    "{{LOGO_LIGHT}}": uri(logo / "hoo-logo-horizontal-light.svg", "image/svg+xml"),
    "{{LOGO_DARK}}": uri(logo / "hoo-logo-horizontal-dark.svg", "image/svg+xml"),
    "{{STACK_LIGHT}}": uri(logo / "hoo-logo-stacked-light.svg", "image/svg+xml"),
    "{{STACK_DARK}}": uri(logo / "hoo-logo-stacked-dark.svg", "image/svg+xml"),
    "{{AV_NIGHT}}": uri(avatar / "hoo-avatar-night-circle.svg", "image/svg+xml"),
    "{{AV_PURPLE}}": uri(avatar / "hoo-avatar-purple-circle.svg", "image/svg+xml"),
    "{{AV_MIST}}": uri(avatar / "hoo-avatar-mist-circle.svg", "image/svg+xml"),
    "{{PHOTO_1}}": uri(here / "p1.webp", "image/webp"),
    "{{PHOTO_2}}": uri(here / "p2.webp", "image/webp"),
    "{{PHOTO_3}}": uri(here / "p3.webp", "image/webp"),
    "{{CORE}}": CORE, "{{SCALE}}": SCALE, "{{LINES}}": LINES, "{{BARS}}": BARS, "{{LEG}}": LEG, "{{TBL}}": TBL,
    "{{DOWNLOADS}}": DOWNLOADS,
    "{{TOKENS_ESC}}": html.escape(tokens_css),
    "{{TOKENS_RAW}}": tokens_css.replace("</script", "<\\/script"),
}
out = (here / "template.html").read_text(encoding="utf-8")
for k, v in rep.items():
    out = out.replace(k, v)
assert "{{" not in out, [x for x in ("{{" + s for s in out.split("{{")[1:2])]
(here / "index.html").write_text(out, encoding="utf-8")
print("index.html", round(len(out.encode()) / 1024), "KB")
