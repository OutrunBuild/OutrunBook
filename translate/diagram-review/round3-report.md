# Round 3 — adversarial review + family-level repair

Scope: all 13 diagrams (manifest below). One fresh adversarial reviewer per diagram; fixes by separate agents; renders via /tmp/render-diagram.py (goto-wrapper bug found in round 3 and fixed; all r4-* renders verified unique).

Manifest: dao-cycle, ecosystem-bite, fee-split, four-pools, genesis-rights, hook-fee, omnichain-stages, polend-settlement, preorder-flow, uasset-supply, verse-lifecycle, yt-flash-buy, yt-flash-sell — src spec `assets/diagrams/src/<name>.*.json`, HTML `assets/diagrams/<name>.html`, baked SVG `assets/diagrams/<name>.svg` (the artifact chapters embed), fact source = linked chapter md.

## Verdicts (all FAIL — loop continues to round 4)

| diagram | P0 | P1 | P2 | verdict | dominant issues |
|---|---|---|---|---|---|
| dao-cycle | 0 | 1 | 7 | FAIL | effective font sizes below 11px floor |
| ecosystem-bite | 1* | 1 | 5 | FAIL | fonts; duplicate/orphan edge labels |
| fee-split | 0 | 2 | 5 | FAIL | "Memecoin-denominated" label detached from its line (misattribution risk); fonts |
| four-pools | 0 | 2 | 7 | FAIL | fonts; label pads cutting lane borders |
| genesis-rights | 1 | 2 | 8 | FAIL | fonts (graded P0 by reviewer); node overflows lane |
| hook-fee | 0 | 3 | 6 | FAIL | "Exempt: base fee only" reads backwards; fonts; pipeline* |
| omnichain-stages | 0 | 2 | 8 | FAIL | send-revert label clipped outside viewBox; fonts |
| polend-settlement | 0 | 3 | 3 | FAIL | "Unified settlement" zero padding; retry edge crosses lane title; treasury wording (protocol → DAO) |
| preorder-flow | 0 | 2 | 6 | FAIL | fonts; arrowhead/line color mismatch |
| uasset-supply | 1* | 1 | 5 | FAIL | fonts; duplicated "Mint at face value"; overlapped dual exit edges |
| verse-lifecycle | 0 | 4 | 4 | FAIL | at-deadline edge invisible under main rail; main-rail arrowhead swallowed by Steady box; fonts; pipeline* |
| yt-flash-buy | 1* | 2 | 3 | FAIL | all 4 message arrows stop 5–6px short of lifelines; fonts |
| yt-flash-sell | 0 | 2 | 6 | FAIL | stale render artifact*; card/note fonts below floor |

\* P0/P1 items marked with an asterisk were **render-pipeline defects** (shared stale wrapper in /tmp/render-diagram.py line 39 made the round-3 pre-rendered PNG batch one single wrong image), not diagram defects. Every reviewer detected it, re-rendered cleanly, and reviewed the true diagram. Script fixed (`goto` now uses the per-invocation wrapper); round-4 renders verified unique by md5.

## Family-level repairs (central, before per-diagram fixes)

Renderer (.agents/skills/archify) + exporter (scripts/export-static-diagrams.py):

1. **Typography tiers raised** so effective sizes at the 820px embed meet the baseline (≥14 titles / ≥12 labels / ≥11 any text): node & state titles 15 (min 12), edge/transition/flow labels 13, lane/stage titles 13, sublabels 12.5 (min 12), tags/classifications/notes/step numbers 12–12.5, legend renders 13, cards 14/12, baked figure title 20. Text-fit minimums enforced by the showcase validator (a label that cannot fit must be widened or shortened — no silent shrink).
2. **Arrowheads inherit their own line's baked stroke** (baked_edge_strokes): gray-on-gray, violet-on-violet, green-on-green — fixes the bright-gray-on-violet and dark-green-on-green mismatches.
3. **Dashed-edge labels turn violet** (variantAccent default `t-database`), killing the unexplained orange third color.
4. **Two-tier text ink** replaces all-white: primary #E6E9F0, muted #C5CDDA, dim/faint #9AA3B5 (≥6:1 on the darkest panel) — no bare white.
5. **Fact cards**: title 14 / body 12, uniform card heights; **figure title** 20.
6. **Sequence arrows** now end 1px short of the lifeline (marker tip lands on it) — fixes the 5–6px float.
7. **Lifecycle main rail** now stops 8px before the terminal state's left edge — its arrowhead is no longer painted over by the Steady-state box.
8. **Workflow/lifecycle geometry enlarged** (laneW 800, colXs scaled; phase pitch 170, boxes 150/160) to host the larger type; dataflow leftX 70.
9. Renderer script /tmp/render-diagram.py goto-wrapper bug fixed.

## Per-diagram fixes (all: validate 0 errors / 0 warnings, 9/9 showcase checks, delivered + self-checked at 820px)

| diagram | round-3 finding → fix |
|---|---|
| dao-cycle | labels off-midpoint → exact midpoints; unlabeled claim→rollover → "Unclaimed"; legend↔cards dead band → viewBox 874×430; spacing rebalanced; short labels ("into the vault") |
| ecosystem-bite | "Genesis Staking / PSM" duplicate → "deposit"; "mint" → "issued"; demand-signal label violet ✓; 61px dead space → viewBox 824×360; lane indents rebalanced; stage title clipping found & fixed in self-check |
| fee-split | "Memecoin-denominated" detached (P1) → routed right→bottom with labelAt on its own trunk, pad masks its own line only; "POL-denominated" moved; viewBox 1080→824; "Staking YieldVault" 9.6 shrink → widened 168; "With referrer" on-axis; long labels condensed ("denominated" semantics carried by node + card) |
| four-pools | 5 stages → 4 ("Mint & split") so viewBox hugs at 824; "~3/7"/"~70%" exact midpoints; pads all ride their lines; stage title overflow → "Mint & split"; out-of-lane route pulled in; emphasis arrowheads same color ✓; NOTE: aux→PT/uAsset edge removed (topologically impossible without a counted crossing at showcase gate) — facts preserved in node sublabel + card |
| genesis-rights | fonts ✓ (min 12.0 effective); overflowing node → "Unlock tx" (152 wide, inside lane); "From Locked" → "At Locked"; lock-up-end semantics moved to a dedicated Lockup anchor node (edge deleted that clipped the fees node); label near-touches staggered; "Resumes at expiry" centered; stage titles ≤21 chars; sigil/title collision found in self-check and fixed; misleading in-unlock edge replaced by Lockup anchor chain |
| hook-fee | "Exempt: base fee only" → "Dynamic fees waived — base fee only" (P1, matches hook.md); dead bands tightened (viewBox 866×510); EWVWAP box moved col3→col2; nodes off lane borders (12/10 clearance); "Pool-opening fee"/"decay fee" unified to "opening fee"; card fact "per address × pool" corrected to per-address + 3s window per hook.md |
| omnichain-stages | clipped send-revert label → rerouted west corridor, labelAt [200,480] fully inside; all 9 state titles hit 15 units (widths/short labels); "Full amount sent" edge removed (rail carries main chain under new geometry); double-arrowhead stack resolved (unique ports); duplicate edge notes removed/reworded ("Only gas is lost"); failure edges = dashed variant + truncation edges default solid + legend entry; dead-end Queued → added "Redelivered automatically" return edge (omnichain.md:34); "extremely rare" → "rare"; chip clearances and card orphans fixed |
| polend-settlement | "Unified settlement" box 120→178, all 11 title paddings ≥8 (measured); retry edge rerouted around lane title (9-unit clearance); card fact fixed to "DAO treasury"; all routes ≥24 from canvas edges; reserve→protect legend collision caught by validator and fixed; viewBox 890×554. Residual: node titles 13.82 / edge labels 11.98 effective (1.3%/0.2% under target — the minimum hug that keeps the right rail off the lane border; documented) |
| preorder-flow | viewBox 1080→824; "Active claim" merged into stage 04 (5 stages impossible at target fonts); "Funds & flow" → "Funds and flows"; "leveraged debt principal" aligned to chapter; node-kind legend entry (Pools) added where schema allows; all 7 labels on midpoints ✓; orange labels / two-tone arrowheads confirmed fixed |
| uasset-supply | viewBox 860→824; duplicate "Mint at face value" → subtitle now "Opens a position"; dual exit edges separated (automatic port spread, green fully visible); card orphan words rewritten; Leveraged Genesis source carried by polend sublabel "Memeverse debt quota" (a cross-lane edge would have dirtied the canvas) |
| verse-lifecycle | at-deadline edge rerouted via bottom channel (clear double通道 with Fast Genesis); main-rail arrowhead → renderer-level fix (stop before terminal box); all titles 15 units (×1.139 scale = 17.1 effective); "How to read the map" card explains rail vs transitions (legend schema has no line-style entries); viewBox drift fixed (720×660); data-detail notes folded into visible labels (viewer hides fine layer at read depth) |
| yt-flash-buy | arrows touch lifelines (4/4, measured 0.4–0.6px); viewBox height 500→480 (schema floor), tail gap 7.9%; legend return+default merged into "Message" (schema-supported); fonts all on target (units = effective px at 820) |
| yt-flash-sell | arrows touch lifelines (4/4); tail gap 81→33px (6.9%); message rows evenly spaced (60px); legend merged (request vs return now color+dash distinguishable); delivery arrow merge→user preserved and verified |

## Effective-size floor audit (baked SVGs, 820px)

min effective font-size per diagram: 11.06 (polend) – 13.67 (verse-lifecycle); **0 text below 11 anywhere**. Node titles 13.8–15.9 (polend 13.82 and hook-fee 13.9 are the two documented ~1% trades); edge labels 11.97–14.1. Marker/line color pairs verified: exact match on all 7 diagrams that have dashed edges; the other 6 carry an unused dashed marker.

## Carried into round 4 (verify items)

- polend/hook title effective sizes 13.82/13.9 vs 14 target (documented tradeoff, judge at review).
- four-pools aux→PT/uAsset edge removal (topology-forced; facts in sublabel+card).
- Lifecycle rail start gap (x=154 vs send box) — family constant, noted by omnichain fixer.
- ecosystem-bite supply-lane indent 38px (canvas-bound minimum).
- family palette still #020617 slate + emerald + JetBrains Mono (P2, consistent across all 13; needs a book-level decision, unchanged this round).
