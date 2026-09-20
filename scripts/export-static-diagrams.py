#!/usr/bin/env python3
"""Export self-contained static SVGs from archify diagram HTMLs (dark theme).

Strategy: computed-style baking. The delivered interactive HTML is opened in
Chromium with the dark theme forced; for every rendered SVG element the
computed fill/stroke/typography is captured and emitted as a deduped CSS
block inside the standalone SVG. This eliminates the whole class of bugs
where textual var() resolution leaked light-theme values into the bake
(white-on-white label chips). Textual resolution is kept only for <defs>
(patterns/markers), which Chromium does not expose via getComputedStyle.

Also, per readability decisions:
- text is never gray: gray text fills are whitened (hierarchy = size/weight);
- decorative node sigils that collide with titles in static rendering are
  hidden;
- the interactive HTML's dark block gets its text variables whitened too.

Run with the playwright venv python after every `archify deliver`:
    /tmp/pwvenv/bin/python scripts/export-static-diagrams.py
"""
import re
import sys
import base64
import pathlib
import xml.etree.ElementTree as ET

REPO = pathlib.Path(__file__).resolve().parent.parent
DIAG = REPO / "assets" / "diagrams"
FONT = DIAG / "fonts" / "jetbrains-mono-subset.woff2"

GRAY_TEXT_FILLS = {
    "#475569", "#64748b", "#7d8da1", "#94a3b8",  # archify palette
    "#8494ab", "#7b8ca4", "#cbd5e1", "#b6c2d4", "#a5b4c9", "#8fa3bd",
}

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

GRAY_RGB = {hex_to_rgb(h) for h in GRAY_TEXT_FILLS}

def rgb_str_is_gray(value: str) -> bool:
    m = re.match(r"(?:rgb|rgba)\((\d+),\s*(\d+),\s*(\d+)", value)
    if not m:
        return False
    r, g, b = (int(m.group(i)) for i in (1, 2, 3))
    return (r, g, b) in GRAY_RGB

# Interactive HTML: text variables in the dark block go white. Stroke and
# fill variables (--arrow, --mask, node fills) keep their designed values.
READABILITY_OVERRIDES = {
    "--text-muted": "#ffffff",
    "--text-dim": "#ffffff",
    "--text-faint": "#ffffff",
}

CAPTURE_PROPS = [
    "fill", "stroke", "stroke-width", "stroke-dasharray", "opacity",
    "fill-opacity", "font-size", "font-weight", "font-family",
    "letter-spacing", "paint-order", "dominant-baseline", "text-anchor",
]
PROP_DEFAULTS = {
    "stroke": "none", "stroke-width": "1", "stroke-dasharray": "none",
    "opacity": "1", "fill-opacity": "1", "letter-spacing": "normal",
    "paint-order": "normal",
}


def strip_at_blocks(css: str) -> str:
    """Remove every @-block (media, keyframes, ...) via brace counting, so the
    flat rule regex below parses the remaining top-level rules correctly."""
    out, i = [], 0
    while True:
        m = re.search(r"@[a-zA-Z-]+[^{;]*\{", css[i:])
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
        i = j
    return "".join(out)


def strip_light_media_blocks(css: str) -> str:
    """Remove @media blocks conditioned on light scheme (brace-counting)."""
    out, i = [], 0
    while True:
        m = re.search(r"@media[^{]*\{", css[i:])
        if not m:
            out.append(css[i:])
            break
        start = i + m.start()
        open_brace = i + m.end() - 1
        depth, j = 1, open_brace + 1
        while j < len(css) and depth:
            if css[j] == "{":
                depth += 1
            elif css[j] == "}":
                depth -= 1
            j += 1
        if "light" not in m.group(0):
            out.append(css[start:j])
        i = j
    return "".join(out)


def strip_comments(css: str) -> str:
    return re.sub(r"/\*[\s\S]*?\*/", "", css)


def parse_rules(css: str):
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
        yield m.group(1), m.group(2)


def build_var_map(css: str) -> dict:
    """Dark-theme variables: :root / [data-theme="dark"] blocks, first wins."""
    vars_ = {}
    for sel, body in parse_rules(css):
        branches = [b.strip() for b in strip_comments(sel).split(",")]
        if not any(b in (":root", '[data-theme="dark"]') for b in branches):
            continue
        for decl in body.split(";"):
            m = re.match(r"\s*(--[\w-]+)\s*:\s*([^;]+)", decl)
            if m and m.group(1) not in vars_:
                vars_[m.group(1)] = m.group(2).strip()
    return vars_


def resolve_vars(value: str, var_map: dict) -> str:
    def sub(match):
        return var_map.get(match.group(1), match.group(2) or "")
    for _ in range(10):
        new = re.sub(r"var\((--[\w-]+)(?:\s*,\s*([^()]*))?\)", sub, value)
        if new == value:
            break
        value = new
    return value


def patch_html_dark_theme(html_path: pathlib.Path) -> str:
    """Whiten text variables in the interactive HTML's dark block."""
    html = html_path.read_text()
    m = re.search(r"(:root\s*,\s*\[data-theme=\"dark\"\]\s*\{)([\s\S]*?)(\})", html)
    if not m:
        return "dark var block not found (skipped)"
    block, patched = m.group(2), m.group(2)
    for var, value in READABILITY_OVERRIDES.items():
        patched = re.sub(rf"({var}\s*:\s*)#[0-9a-fA-F]{{6}}", rf"\g<1>{value}", patched)
    if patched != block:
        html_path.write_text(html[: m.start(2)] + patched + html[m.end(2):])
        return "HTML dark block patched"
    return "HTML already patched"


def extract_defs(svg: str, var_map: dict) -> str:
    """Keep <defs> as authored, with variables resolved textually."""
    m = re.search(r"<defs[\s\S]*?</defs>", svg)
    if not m:
        return ""
    defs = m.group(0)
    return resolve_vars(defs, var_map)


def bake_computed(html_path: pathlib.Path, svg: str, var_map: dict):
    """Capture computed styles from the dark-rendered HTML and return CSS."""
    from playwright.sync_api import sync_playwright

    chrome = pathlib.Path.home() / ".cache/ms-playwright/chromium-1234/chrome-linux64/chrome"
    import os
    env = {**os.environ}
    if "LD_LIBRARY_PATH" in os.environ:
        env["LD_LIBRARY_PATH"] = os.environ["LD_LIBRARY_PATH"]
    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            executable_path=str(chrome), args=["--no-sandbox"], env=env)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.goto(f"file://{html_path}?theme=dark&embed=1")
        page.evaluate("document.documentElement.setAttribute('data-theme','dark')")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(400)
        bg = page.evaluate(
            "getComputedStyle(document.body).backgroundColor")
        records = page.evaluate(
            """
            () => {
              const svg = document.querySelector('svg');
              const out = [];
              for (const el of svg.querySelectorAll('*')) {
                if (el.closest('defs')) continue;
                const tag = el.tagName.toLowerCase();
                if (!['g','rect','path','text','tspan','line','circle','ellipse',
                      'polygon','polyline','use'].includes(tag)) continue;
                const cs = getComputedStyle(el);
                const props = {};
                for (const p of ['fill','stroke','stroke-width','stroke-dasharray',
                                 'opacity','fill-opacity','font-size','font-weight',
                                 'font-family','letter-spacing','paint-order',
                                 'text-anchor','dominant-baseline']) {
                  props[p] = cs[p];
                }
                const isTextEl = ['text','tspan'].includes(tag);
                const anchor = isTextEl ? cs['text-anchor'] : '';
                const baseline = isTextEl ? cs['dominant-baseline'] : '';
                const dataAttrs = [...el.attributes]
                  .filter(a => a.name.startsWith('data-'))
                  .map(a => a.name + '=' + a.value).sort().join('\\x1f');
                out.push({tag, cls: el.getAttribute('class') || '',
                          data: dataAttrs, props, anchor, baseline});
              }
              return out;
            }
            """
        )
        browser.close()

    # dedupe by (tag, class, data-signature); first occurrence wins
    seen, rules = {}, []
    for rec in records:
        key = (rec["tag"], rec["cls"], rec["data"])
        if key in seen:
            continue
        seen[key] = True
        decls = []
        tag = rec["tag"]
        cls_sel = "".join("." + c for c in rec["cls"].split())
        # quoted attribute selectors: values may contain commas/spaces; a
        # bare [name] per fragment produced invalid selectors, which drop
        # the whole CSS rule and default fills bleed through (black wedges).
        # fragments are joined on \x1f (unit separator), never on ";": data
        # values themselves contain ";" (multi-point composition routes), so
        # a ";" split shattered selectors like data-composition-points into
        # invalid [x,y=""] fragments and dropped every multi-segment edge rule
        attr_sels = ""
        for d in rec["data"].split("\x1f"):
            if not d:
                continue
            name, _, value = d.partition("=")
            attr_sels += "[" + name + '="' + value.replace("\\", "\\\\").replace('"', '\\"') + '"]'
        sel = tag + cls_sel + attr_sels
        props = rec["props"]
        is_text = tag in ("text", "tspan")
        is_container = tag in ("g", "use")
        is_bare = not rec["cls"] and not rec["data"]
        if is_bare and not is_text:
            # bare shapes are styled by presentation attributes already; a
            # tag-only rule (e.g. rect -> grid pattern fill) would leak onto
            # every same-tag element
            continue
        for prop, value in props.items():
            value = (value or "").strip()
            if not value or value == PROP_DEFAULTS.get(prop):
                continue
            if prop in ("fill", "stroke", "stroke-width", "stroke-dasharray") and is_container:
                continue
            if prop in ("font-size", "font-weight", "font-family", "letter-spacing",
                        "paint-order") and not is_text:
                continue
            # text-anchor/dominant-baseline are per-element positional values,
            # not class traits — dedupe would leak one element's anchoring
            # onto every sibling (legend text centered onto its icons)
            if prop in ("text-anchor", "dominant-baseline"):
                continue
            if prop == "fill" and value == "rgba(0, 0, 0, 0)":
                continue
            # for shapes, fill:none must be EMITTED: standalone SVGs default
            # to black fill, the HTML stylesheet default was none — dropping
            # the declaration paints route paths as giant black wedges
            if prop == "fill" and value == "none" and is_text:
                continue
            if prop == "font-weight" and value == "400":
                continue
            if is_text and prop == "fill" and rgb_str_is_gray(value):
                value = "rgb(255, 255, 255)"
            # detail toggles (data-detail) hide content in the interactive
            # viewer only — the static artifact must show everything
            if prop == "opacity" and value == "0" and "data-detail" in rec["data"]:
                value = "1"
            # accent-colored tag text (t-backend teal) sits on its own node's
            # tinted fill — near-invisible; tags carry facts, use white ink
            if (is_text and prop == "fill" and value == "rgb(52, 211, 153)"
                    and "data-detail" in rec["data"]):
                value = "rgb(255, 255, 255)"
            # same for the violet t-database tag (e.g. "Pegged stablecoin")
            # on the violet database-node surface — ~3.5:1 at 7px
            if (is_text and prop == "fill" and value == "rgb(167, 139, 250)"
                    and "data-detail" in rec["data"]):
                value = "rgb(255, 255, 255)"
            decls.append(f"{prop}: {value}")
        if decls:
            rules.append(f"{sel} {{ " + "; ".join(decls) + "; }")
    css = "\n".join(rules)
    # per-element positional attributes for every text/tspan, in document order
    overrides = [
        (rec["anchor"], rec["baseline"]) for rec in records
        if rec["tag"] in ("text", "tspan")
    ]
    return css, bg, overrides


def defs_class_rules(css_text: str, svg: str, var_map: dict) -> str:
    """Textual rules for classes used only inside <defs> (patterns, markers).

    Chromium's getComputedStyle is unreliable for non-rendered defs content,
    so pattern/marker styling (c-grid, m-*) is resolved from the stylesheet
    directly. Without these, pattern paths render black-filled (diagonal
    slabs) and markers lose their fill.
    """
    needed = set()
    defs = re.search(r"<defs[\s\S]*?</defs>", svg)
    if defs:
        needed.update(re.findall(r'class="([^"]+)"', defs.group(0)))
    if not needed:
        return ""
    # authored semantic rules, rebuilt from the dark variable map (parsing
    # the full stylesheet is fragile; these classes have exactly one meaning)
    var = lambda name: var_map.get(name, "#64748b")
    authored = {
        "c-grid": f"fill: none; stroke: {var('--grid')};",
        "m-default": f"fill: {var('--arrow')};",
        "m-dashed": f"fill: {var('--arrow')};",
        "m-emphasis": f"fill: {var('--arrow-emphasis')};",
        "m-security": f"fill: {var_map.get('--arrow-security') or var('--arrow')};",
    }
    rules = []
    for cls in sorted(needed):
        if cls in authored:
            rules.append(f".{cls} {{ {authored[cls]} }}")
    return "\n".join(rules)


CARD_DOTS = {
    "cyan": "#22d3ee", "violet": "#a78bfa", "rose": "#fb7185",
    "emerald": "#34d399", "amber": "#fbbf24", "orange": "#fb923c",
}


def wrap_text(text: str, width: int) -> list:
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= width:
            cur = f"{cur} {w}".strip()
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def render_cards(svg: str, cards: list, bg: str) -> str:
    if not cards:
        return svg
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    W, H = float(vb.group(1)), float(vb.group(2))
    margin, gap, pad = 24, 16, 12
    card_w = (W - 2 * margin - (len(cards) - 1) * gap) / len(cards)
    char_w = 4.9  # ~8px JetBrains Mono advance
    wrap_at = max(24, int((card_w - 2 * pad - 10) / char_w))
    panel = "#1e293b"  # dark slate border (authored card chrome)
    # measure
    heights = []
    for card in cards:
        n_lines = sum(len(wrap_text(it, wrap_at)) for it in card.get("items", []))
        heights.append(20 + 14 + n_lines * 11 + pad)
    row_h = max(heights) + pad
    # widen the root viewBox (first occurrence in the open tag)
    svg = re.sub(r'viewBox="0 0 [\d.]+ [\d.]+"',
                 f'viewBox="0 0 {W:g} {H + row_h:g}"', svg, count=1)
    g = [f'<g id="cards" font-family="JetBrains Mono, monospace">']
    g.append(f'<rect x="0" y="{H:g}" width="{W:g}" height="{row_h:g}" fill="{bg}"/>')
    for idx, card in enumerate(cards):
        x = margin + idx * (card_w + gap)
        y = H + pad / 2
        g.append(
            f'<rect x="{x:g}" y="{y:g}" width="{card_w:g}" height="{heights[idx]:g}" rx="8" '
            f'fill="rgba(15, 23, 42, 0.55)" stroke="{panel}" stroke-width="1"/>')
        dot = CARD_DOTS.get(card.get("dot", ""), "#ffffff")
        g.append(f'<circle cx="{x + pad + 3:g}" cy="{y + 12:g}" r="3" fill="{dot}"/>')
        g.append(f'<text x="{x + pad + 12:g}" y="{y + 15:g}" fill="#ffffff" '
                 f'font-size="10" font-weight="600">{card.get("title", "")}</text>')
        ty = y + 32
        for item in card.get("items", []):
            for line in wrap_text(item, wrap_at):
                g.append(f'<text x="{x + pad + 3:g}" y="{ty:g}" fill="#ffffff" '
                         f'font-size="8">{line}</text>')
                ty += 11
    g.append("</g>")
    return svg.replace("</svg>", "".join(g) + "</svg>")


def render_svg_title(svg: str, title: str) -> str:
    """Bake meta.title as a visible header line (opt-in via titleInSvg).

    The standalone SVG is what chapters embed; without this the title exists
    only as an invisible a11y <title>.
    """
    esc = title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    g = (
        '<g id="svg-title">'
        f'<text x="24" y="30" fill="#ffffff" font-size="13" font-weight="600" '
        f'font-family="JetBrains Mono, monospace">{esc}</text></g>'
    )
    return svg.replace("</svg>", g + "</svg>")


def export_one(html_path: pathlib.Path):
    html = html_path.read_text()
    svg_m = re.search(r"<svg[\s\S]*?</svg>", html)
    if not svg_m:
        return (html_path.name, 0, "no <svg> found")
    svg = svg_m.group(0)
    css_text = strip_light_media_blocks(
        strip_comments("\n".join(re.findall(r"<style[^>]*>([\s\S]*?)</style>", html))))
    var_map = build_var_map(css_text)

    computed_css, bg, text_overrides = bake_computed(html_path, svg, var_map)
    if not computed_css:
        return (html_path.name, 0, "computed capture empty")
    css_raw = strip_comments("\n".join(re.findall(r"<style[^>]*>([\s\S]*?)</style>", html)))

    root_open = svg[: svg.index(">") + 1]
    if "xmlns=" not in root_open:
        svg = svg.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" ', 1)
    defs = extract_defs(svg, var_map)
    if defs:
        svg = re.sub(r"<defs[\s\S]*?</defs>", defs, svg, count=1)

    font_face = ""
    if FONT.exists():
        b64 = base64.b64encode(FONT.read_bytes()).decode()
        font_face = (
            "@font-face { font-family: 'JetBrains Mono'; font-style: normal; "
            "font-weight: 100 800; "
            f"src: url(data:font/woff2;base64,{b64}) format('woff2'); }}"
        )
    else:
        print(f"warning: {FONT} missing; fallback fonts will be used", file=sys.stderr)

    style_block = (
        "<style type=\"text/css\"><![CDATA[\n"
        + font_face + "\n"
        + "svg .semantic-sigil { display: none; }\n"
        + defs_class_rules(css_raw, svg, var_map) + "\n"
        + computed_css + "\n"
        + "]]></style>"
    )
    bg_rect = f'<rect x="0" y="0" width="100%" height="100%" fill="{bg}"/>'
    insert_at = svg.index(">") + 1
    svg = svg[:insert_at] + style_block + bg_rect + svg[insert_at:]

    # write per-element anchoring back as attributes, in document order
    state = {"i": 0}

    def add_anchor(m):
        tag, attrs = m.group(1), m.group(2)
        idx = state["i"]
        state["i"] += 1
        if idx >= len(text_overrides):
            return m.group(0)
        anchor, baseline = text_overrides[idx]
        add = ""
        if anchor and anchor != "start" and "text-anchor=" not in attrs:
            add += f' text-anchor="{anchor}"'
        if (baseline and baseline not in ("auto", "")
                and "dominant-baseline=" not in attrs):
            add += f' dominant-baseline="{baseline}"'
        return f"<{tag}{attrs}{add}>"

    svg = re.sub(r"<(text|tspan)((?:[^>])*)>", add_anchor, svg)
    assert state["i"] == len(text_overrides), (
        f"anchor writeback mismatch: {state['i']} vs {len(text_overrides)}")

    # fact cards: the interactive page renders them as HTML sections below
    # the diagram — bake them into the standalone SVG or the facts are lost
    import json
    src_jsons = sorted((DIAG / "src").glob(f"{html_path.stem}.*.json"))
    if src_jsons:
        try:
            src = json.loads(src_jsons[0].read_text())
            if src.get("meta", {}).get("titleInSvg") and src.get("meta", {}).get("title"):
                svg = render_svg_title(svg, src["meta"]["title"])
            cards = src.get("cards", [])
            if cards:
                svg = render_cards(svg, cards, bg)
        except (json.JSONDecodeError, OSError) as e:
            print(f"warning: cards not baked for {html_path.name}: {e}",
                  file=sys.stderr)

    try:
        ET.fromstring(svg)
    except ET.ParseError as e:
        return (html_path.name, 0, f"invalid XML: {e}")

    out = html_path.with_suffix(".svg")
    out.write_text(svg)

    # guards: leftover gray TEXT fills or unresolved vars = palette drift.
    # Scoped to text rules/elements — slate hexes legitimately survive as
    # arrow marker fills (m-*) and lane strokes.
    gray_left = []
    for m in re.finditer(r"(text\.[^\n{]*|<text[^>]*?)fill:\s*(#[0-9a-fA-F]{6})", svg):
        if m.group(2).upper() in {h.upper() for h in GRAY_TEXT_FILLS}:
            gray_left.append(m.group(2))
    residue = "var(--" in svg.replace("<defs", "", 1) if "<defs" in svg else "var(--" in svg
    html_status = patch_html_dark_theme(html_path)
    status = "OK"
    if residue:
        status = "OK (UNRESOLVED var residue outside defs!)"
    if gray_left:
        status += f" (GRAY FILL LEFT: {','.join(sorted(set(gray_left)))}!)"
    return (html_path.name, len(computed_css.splitlines()), f"{status} | {html_status}")


def main() -> int:
    htmls = sorted(DIAG.glob("*.html"))
    if not htmls:
        print("no diagram HTMLs found", file=sys.stderr)
        return 1
    bad = 0
    for name, n, status in (export_one(h) for h in htmls):
        print(f"{name:28s} rules={n:4d}  {status}")
        if "OK" not in status or "!" in status:
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
