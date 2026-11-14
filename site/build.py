"""把 index.src.html 里的图片和 logo 内联，生成单文件 index.html。
用法：python3 site/build.py
"""
import base64, re, pathlib

root = pathlib.Path(__file__).parent
logo_dir = root.parent / "logo" / "final"
src = (root / "index.src.html").read_text(encoding="utf-8")


def inline_svg(name: str) -> str:
    s = (logo_dir / name).read_text(encoding="utf-8").strip()
    return s.replace("<svg ", '<svg role="img" aria-hidden="true" focusable="false" ', 1)


def img_uri(m: re.Match) -> str:
    data = (root / "img" / f"{m.group(1)}.webp").read_bytes()
    return "data:image/webp;base64," + base64.b64encode(data).decode()


out = re.sub(r"\{\{img:([a-z0-9-]+)\}\}", img_uri, src)
out = out.replace("{{logo-dark}}", inline_svg("hoo-logo-horizontal-dark.svg"))
(root / "index.html").write_text(out, encoding="utf-8")
print("index.html", round(len(out.encode()) / 1024), "KB")
