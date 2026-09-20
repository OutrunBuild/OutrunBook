# verse-lifecycle review (round 1)

Reviewed: assets/diagrams/verse-lifecycle.svg (rendered at 820px and 1100px) against memeverse/lifecycle.md + memeverse/genesis.md. Source JSON: assets/diagrams/src/verse-lifecycle.lifecycle.json. Known global issues (label-chip white-on-white, gray-text dimness) excluded.

## P1

- [图形错误] All three content cards are missing from the exported SVG — src JSON defines "Either threshold suffices" / "Phase advances are transaction-triggered" / "Two exits" and the HTML contains them, but the SVG (what lifecycle.md line 7 actually embeds) has zero occurrences of the card text; the diagram's core fact "either threshold suffices" appears nowhere in the published image. → export script: render the cards block into the SVG path (or, if cards are main-track-only, move "either threshold suffices" into an edge/state label so the fact survives).

- [字体] At 820px every text is far below readable size (viewBox 980 scaled 0.837x): state titles 10→8.4px, edge labels 8→6.7px, sublabels 6.7–7→5.6–5.9px, note "Public trading resumes…" →5.9px, lane labels →8.4px; even at 1100px edge labels are only 9px. → export script: raise SVG-space font sizes (state titles ≥14, edge labels ≥11, sublabels ≥9.5) or shrink the viewBox so the same width renders larger type.

- [颜色搭配] White-on-tint state text: each state box is a white `c-mask` base under a 40% color overlay, producing light fills (Genesis light slate-teal, Locked light sage, Unlocked light sage, Steady state light lilac, Refund dusty pink), while `t-primary` titles and `t-muted` sublabels are #fff — ~1.5–2:1 contrast on every box ("Genesis", "Locked", "Unified settlement + 24h", "Refund" etc.). Distinct from the label-chip bug: these are the state boxes themselves. → export script: dark text on the light tint fills (or dark fills with light text) — one pairing rule for title/sublabel/step-chip text.

- [排列布局] Fast Genesis label plate (rect x45–297, y85–101) is drawn after and completely covers the "01 / Main track" lane label (x72, baseline y100 — glyphs y92–102 inside the plate area): the first lane renders with no visible label. → src JSON: move `labelAt` for to-locked-flash down/right of the lane header (y ≥ 112 or x > 300); export script: add a plate-vs-lane-label overlap check.

- [排列布局] The to-refund edge's vertical drop at x≈94 (y188→306) passes straight through the "02 / Branch track" lane label (x72–~157, baseline y252). → src JSON: exit Genesis from bottom-right instead of bottom-center, or shift lane labels right of the routing channel; export script: route-aware lane-label placement.

- [排列布局] Lane "02 / Branch track" is empty — no state is assigned to it in src JSON (refund goes to terminal), so the band holds nothing but the passing refund edge and its floating label; a named, ruled, empty lane reads as missing content. → src JSON: delete the branch lane (two-lane layout: main + missed-threshold exit) or place real content in it.

## P2

- [箭头形状] Edge labels detach from their arrows and float in the dead band: "No Fast Genesis: at deadline" plate sits ~48px below the Genesis→Locked arrow; "Lock-up ends; anyone triggers unified settlement" (labelDy 88) sits ~70px below the Locked→Unlocked arrow; "Protection window ends, auto-resume" (labelDy 55) instead crowds to within 3px of the Unlocked box bottom and reads as a box caption. → src JSON: cut labelDy to ~20–30 and drop labelAt overrides; let the exporter place labels on their edges.

- [排列布局] Large dead bands: content ends at x615 in a 980-wide viewBox (right ~37% empty beyond the dashed lane rules), y0–85 top band empty (no visible title), y508–604 empty between the Refund box and the Legend. → export script: tighten the viewBox to content bounds.

- [图形错误] meta.title "Memecoin lifecycle: from Genesis to steady state" is not rendered visually in the SVG (only the a11y `<title>`; the visible h1 exists only in the HTML viewer). → export script: draw meta.title as a visible heading element in the SVG.

- [颜色搭配] The to-refund edge uses the default gray stroke (#8fa3bd) while the success rail gets green emphasis — the failure/refund path, the diagram's risk message, is the least emphasized line and doesn't match the red Refund box. → export script: style failure transitions with the security/red emphasis pair.

- [产品语义] "Lock-up ends; anyone triggers unified settlement" — no doc supports the actor "anyone"; lifecycle.md and genesis.md only say the advance is "the transaction that actually moves the Verse to Unlocked". → src JSON: reword to "Lock-up ends; transaction triggers unified settlement".

- [产品语义] "No Fast Genesis: at deadline" states no condition while its sibling refund edge does ("neither threshold met") — as drawn the deadline alone appears to advance to Locked, but lifecycle.md requires a threshold met plus a triggered transaction. → src JSON: "No Fast Genesis: threshold met, triggered at deadline".

- [颜色搭配] Locked tag "Four pools deployed" is green (#34d399, 7px) on the light sage box fill — green-on-green-tint, lower contrast than the white sublabels around it. → export script: dark tag text on light fills.
