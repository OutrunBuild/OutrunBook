# ecosystem-bite review (round 1)

Reviewed: assets/diagrams/ecosystem-bite.svg (dark, README-embedded) + ecosystem-bite.html (light) at 820px and 1100px. Note: `/tmp/render-diagram.py` intermittently renders this SVG blank (file:// `<img>` from an `about:blank` page fails to load); a same-origin wrapper render was used for all findings below.

## P1

- [排列布局] Massive dead bands top and bottom, unchanged from history: all content sits in physical y≈355–520 of 972 (an ~17% band); the dashed stage lanes span y≈140–855 with ≈56% of their interior empty (lane tops y140 to first label y≈347, and channel y≈520 to lane bottom y≈855). The 1100px render has the same proportions. → Fix in src JSON geometry: shrink `meta.viewBox` height from 640 to ~360 (and let width-bound scale-up enlarge text), or move `row: 1` content to vertical center and cut lane height; export script must not stretch lanes to the old height.

- [字体] Text is unreadable at the 820px docs width — the #1 historical complaint, quantified. SVG `font-size` × scale 820/1080 = 0.759: node labels 10 → 7.6px effective (supply node 9.6 → 7.3px), flow-label chips 9–10 → 6.8–7.6px, node sublabels 8 → 6.1px, tags ("wstETH · sUSDS · sUSDe…", "lifeline between modules") 7 → 5.3px. Nothing on the canvas reaches 9px. → Fix in src JSON/export script: raise base sizes (labels ≥14, sublabels ≥11, tags ≥10 in viewBox units) and/or shrink viewBox so the 820px scale-up factor exceeds 1.

- [图形错误] The interlock flow (`bite-back`, the diagram's whole point) renders broken: source path `M 745 300 L 745 326 L 530 326 L 530 300` puts the horizontal bottom-channel segment at vb y=326, and the label chip is centered at `labelAt [637, 332]` with an opaque white background — the chip fully covers the horizontal segment. Visible result in both themes: a dashed stub under Memeverse that ends mid-air at the chip edge, and an orphan arrowhead poking up into uAsset's bottom edge with no line attached; the arrow reads as originating from the label text. → Fix in src JSON `flows[bite-back].labelAt`: move y from 332 to ≥352 (clearly below the channel), or place the label above the nodes; keep the channel visible.

- [颜色搭配] uAsset node text contrast fails on the dark SVG (the README-embedded artifact): white "uAsset" label on light-violet fill rgb(183,165,213) ≈ 2.2:1 (needs 4.5:1); the tag "lifeline between modules" rgb(182,158,236) on the same fill ≈ 1.05:1 — effectively invisible. → Fix in export script theme: database-node text should be dark ink on this light fill (or darken the fill); tag color must differ from fill by ≥3:1.

- [图形错误] Text overlap inside the uAsset node: the tag "lifeline between modules" renders on top of the sublabel "UETH/UUSD/UBNB" — doubled, garbled glyphs visible in the 820px and 1100px renders. The node has no room for a third text row. → Fix in src JSON/export geometry: increase database-node height or move the tag outside/below the node; do not stack label+sublabel+tag in a fixed-height box.

- [图形错误] Supply node (`width: 124`) is too narrow: the type icon overlaps the first glyph of the label ("OutStake supply side" collides with the icon), and sublabel "multi-protocol yield assets" plus tag "wstETH · sUSDS · sUSDe…" run edge-to-edge with ~4px padding — visually clipped. Its label was also auto-shrunk to 9.6 vs 10 for the others. → Fix in src JSON: `nodes[supply].width` 124 → ~150 (and re-check mint/uasset widths for icon clearance).

- [产品语义] Legend mislabels the core flow: the violet dashed arrow (bite-back, the supply-demand interlock) is keyed as "async batch" — message-bus vocabulary that contradicts flywheel.md's framing ("The dashed interlock is supply and demand, not yield distribution") and falsely implies a batch-job mechanic. → Fix in src JSON `meta.legend.entries`: override the dashed variant label to e.g. "demand signal — no yields flow back".

## P2

- [产品语义/箭头形状] "Two-way supply-demand interlock" is drawn one-way only: the dashed return leg stops at uAsset's bottom edge, but flywheel.md/README say the demand loop closes as "more people mint on OutStake" — visually the flywheel dead-ends at uAsset instead of returning to Mint/OutStake. Consider routing the dashed arrow back to the "Mint uAsset" node (or annotate the chip with ⇄).
- [颜色搭配] Flow-label chips have low text contrast on white: emerald "Genesis Staking / PSM" and "mint" ≈ 2.3:1, orange interlock chip text ≈ 2.5:1. Darken chip text to 600–700 shades in the export script.
- [图例] Dead legend entry: "Modules and flows" (plain white arrow) matches no flow drawn — it is the un-suppressed `default` entry (`legend.entries.default.visible: true`). Set it false in src JSON.
- [图例] "uAsset assets" entry is redundant wording and its "ⓘ1" superscript footnote (HTML only) resolves to nothing visible in the SVG; rename to "uAsset (UETH/UUSD/UBNB)" and drop or wire the footnote.
- [箭头形状] Emphasis arrowheads are oversized (~2× the stroke weight of the 1.4px lines, larger than node sublabel text); they read as blobs at 820px. Halve marker scale in the export script.
- [排列布局] The wide chip "Genesis funding · leverage interest · Preorder · settlement denomination" crowds the Memeverse node's top border (gap ≈ 10 physical px) and extends left past uAsset's lane boundary; nudge `labelAt [638,232]` up ~12vb or shorten the label.

Semantics otherwise verified against README.md and ecosystem/flywheel.md: lifeline framing correct (meta title, stage "03 / Lifeline", card 3); supply side = Genesis Staking + PSM ✓; use side = Genesis funding · leverage interest · Preorder · settlement denomination ✓; "yields do not flow back" caveat present in both the dashed-flow label and card 2 ✓.
