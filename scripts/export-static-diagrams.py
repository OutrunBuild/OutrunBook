#!/usr/bin/env python3
"""Export self-contained static SVGs from archify diagram HTMLs (dark theme).

For each assets/diagrams/<name>.html this extracts the inline <svg>, bakes the
dark-theme CSS variables and rules into an embedded <style> block, and injects
a full-size background rect (the interactive page normally paints the bg on
<body>, which does not exist in a standalone SVG). Output: <name>.svg next to
the HTML. Re-run after every `archify deliver`.
"""
import re
import sys
import pathlib
import xml.etree.ElementTree as ET

REPO = pathlib.Path(__file__).resolve().parent.parent
DIAG = REPO / "assets" / "diagrams"

SVG_ELEMENTS = {
    "svg", "g", "rect", "path", "text", "tspan", "line", "circle", "ellipse",
    "polygon", "polyline", "defs", "marker", "use", "image", "title", "desc",
    "linearGradient", "radialGradient", "stop", "filter", "pattern", "feDropShadow",
}
EXCLUDE_TOKENS = (
    ":hover", ":focus", ":active", "[data-theme=\"light\"]",
    "html", "body", ".toolbar", "button", "header", "footer", ".theme-toggle",
    ".panel", ".hint", ".zoom", ".menu",
)


def strip_comments(css: str) -> str:
    return re.sub(r"/\*[\s\S]*?\*/", "", css)


def strip_light_media_blocks(css: str) -> str:
    """Remove @media blocks conditioned on light scheme (brace-counting scan).

    A flat regex cannot nest braces, so a `@media (prefers-color-scheme: light)`
    wrapper would leak its inner `:root`/rules into the dark bake.
    """
    out = []
    i = 0
    while True:
        m = re.search(r"@media[^{]*\{", css[i:])
        if not m:
            out.append(css[i:])
            break
        start = i + m.start()
        out.append(css[i:start])
        open_brace = i + m.end() - 1
        depth, j = 1, open_brace + 1
        while j < len(css) and depth:
            if css[j] == "{":
                depth += 1
            elif css[j] == "}":
                depth -= 1
            j += 1
        condition = m.group(0)
        if "light" not in condition:
            out.append(css[start:j])
        i = j
    return "".join(out)


def parse_rules(css: str):
    """Yield (selector_list, body) pairs, ignoring @-rules and nesting braces."""
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
        yield m.group(1), m.group(2)


def build_var_map(css: str) -> dict:
    """CSS variables from :root / [data-theme="dark"] blocks (dark is default).

    First declaration wins: the dark palette is authored first in the
    stylesheet, and any later stray :root block must not override it.
    """
    vars_ = {}
    for sel, body in parse_rules(css):
        sel_clean = strip_comments(sel)
        branches = [b.strip() for b in sel_clean.split(",")]
        if not any(b in (":root", '[data-theme="dark"]') for b in branches):
            continue
        for decl in body.split(";"):
            m = re.match(r"\s*(--[\w-]+)\s*:\s*([^;]+)", decl)
            if m and m.group(1) not in vars_:
                vars_[m.group(1)] = m.group(2).strip()
    return vars_


def resolve_vars(value: str, var_map: dict) -> str:
    def sub(match):
        name = match.group(1)
        fallback = match.group(2)
        if name in var_map:
            return var_map[name]
        return fallback if fallback is not None else ""
    for _ in range(10):
        new = re.sub(r"var\((--[\w-]+)(?:\s*,\s*([^()]*))?\)", sub, value)
        if new == value:
            break
        value = new
    return value


def collect_rules(css: str, svg_classes: set, var_map: dict) -> list:
    rules = []
    for sel, body in parse_rules(css):
        sel_clean = strip_comments(sel)
        if not sel_clean.strip() or sel_clean.strip().startswith("@"):
            continue
        kept = []
        for branch in sel_clean.split(","):
            b = branch.strip()
            if not b or any(tok in b for tok in EXCLUDE_TOKENS):
                continue
            b = re.sub(r'\[data-theme="dark"\]\s*', "", b)
            if not b or b == ":root":
                continue
            # keep if the branch names an svg class or is a bare svg element
            classes_in_b = set(re.findall(r"\.([A-Za-z][\w-]*)", b))
            ids = re.findall(r"#([\w-]+)", b)
            type_sels = set(re.findall(r"(?:^|[\s>+~])([a-z]+)", b))
            touches_svg = (
                classes_in_b & svg_classes
                or (ids and any(i in svg_classes for i in ids))
                or (type_sels & SVG_ELEMENTS and not classes_in_b and not ids)
            )
            if touches_svg:
                kept.append(b)
        if kept:
            body_resolved = resolve_vars(body, var_map)
            if "var(--" not in body_resolved:
                rules.append((", ".join(kept), body_resolved.strip()))
    return rules


def export_one(html_path: pathlib.Path) -> tuple:
    html = html_path.read_text()
    svg_m = re.search(r"<svg[\s\S]*?</svg>", html)
    if not svg_m:
        return (html_path.name, 0, "no <svg> found")
    svg = svg_m.group(0)
    css = "\n".join(re.findall(r"<style[^>]*>([\s\S]*?)</style>", html))
    css = strip_light_media_blocks(css)
    var_map = build_var_map(css)
    if "--bg" not in var_map:
        return (html_path.name, 0, "no --bg variable found")
    svg_classes = set()
    for cls in re.findall(r'class="([^"]+)"', svg):
        svg_classes.update(cls.split())
    rules = collect_rules(css, svg_classes, var_map)
    bg = var_map["--bg"]

    root_open = svg[: svg.index(">") + 1]
    if "xmlns=" not in root_open:
        new_open = root_open.replace(
            "<svg ", '<svg xmlns="http://www.w3.org/2000/svg" ', 1
        )
        svg = new_open + svg[len(root_open):]
    if "xlink:" in svg and "xmlns:xlink" not in svg[: svg.index(">")]:
        svg = svg.replace(
            "<svg ", '<svg xmlns:xlink="http://www.w3.org/1999/xlink" ', 1
        )

    style_block = (
        "<style type=\"text/css\"><![CDATA[\n"
        + "\n".join(f"{sel} {{ {body} }}" for sel, body in rules)
        + "\n]]></style>"
    )
    bg_rect = f'<rect x="0" y="0" width="100%" height="100%" fill="{bg}"/>'
    # insert as the first children inside the root element
    insert_at = svg.index(">") + 1
    svg = svg[:insert_at] + style_block + bg_rect + svg[insert_at:]

    # XML validity check
    try:
        ET.fromstring(svg)
    except ET.ParseError as e:
        return (html_path.name, 0, f"invalid XML: {e}")

    out = html_path.with_suffix(".svg")
    out.write_text(svg)
    residue = "var(--" in svg
    return (html_path.name, len(rules), f"OK{' (UNRESOLVED var residue!)' if residue else ''}")


def main() -> int:
    htmls = sorted(DIAG.glob("*.html"))
    if not htmls:
        print("no diagram HTMLs found", file=sys.stderr)
        return 1
    bad = 0
    for name, n, status in (export_one(h) for h in htmls):
        print(f"{name:28s} rules={n:3d}  {status}")
        if not status.startswith("OK") or "residue" in status:
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
