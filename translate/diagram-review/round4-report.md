# Round 4 — independent re-review (fresh reviewers, all 13)

Verdicts: **3 PASS / 10 FAIL**.

| diagram | P0 | P1 | P2 | verdict | new P1 root cause |
|---|---|---|---|---|---|
| dao-cycle | 0 | 1 | 3 | FAIL | 5 node titles auto-shrank below 14 effective (fitter vs box width) |
| ecosystem-bite | 0 | 1 | 1 | FAIL | card titles (14px) overflow card bounds — family regression from the card font bump |
| fee-split | 0 | 1 | 0 | FAIL | card 3 title clipped at viewBox edge (same family cause) |
| four-pools | 0 | 0 | 1 | PASS | aux-edge removal adjudicated P2-not-misleading (edge+sublabel+card triple-redundant) |
| genesis-rights | 0 | 1 | 1 | FAIL | card 1 title collides into card 2 (same family cause) |
| hook-fee | 0 | 1 | 1 | FAIL | baked CSS class rule `text.t-primary[…] {font-size:15px}` overrides per-node fitted sizes → 3 titles overflow |
| omnichain-stages | 0 | 1 | 4 | FAIL | card titles collide across seams (same family cause) |
| polend-settlement | 0 | 2 | 1 | FAIL | svg-title (81 chars @20px) clipped at right edge; title overlaps a label chip |
| preorder-flow | 0 | 0 | 0 | PASS | — |
| uasset-supply | 0 | 1 | 3 | FAIL | one node title at 14.43 effective (box 156 too narrow) |
| verse-lifecycle | 0 | 2 | 1 | FAIL | card titles collide/clip (family cause); main-rail arrowhead STILL swallowed — the renderer railEnd patch landed after the HTML was delivered, and the SVG was baked from the stale HTML |
| yt-flash-buy | 0 | 0 | 0 | PASS | — |
| yt-flash-sell | 0 | 0 | 3 | PASS | cross-pair legend-naming inconsistency filed P2 |

All round-3 P0/P1 items verified resolved by the fresh reviewers except the two family regressions above (card titles, CSS font-size override) and the stale-HTML rail.

# Round 5 — repair

Central (exporter):

1. **font-size removed from deduped baked CSS rules** — every text element keeps its own font-size attribute, so fitted sizes render as fitted (kills the whole "one rule forces the first element's size onto its signature group" class).
2. **Card titles measured and wrapped** (up to 2 lines, card height grows accordingly) — kills the title-overflow class across all 13.
3. verse-lifecycle + omnichain-stages re-delivered so the lifecycle railEnd patch takes effect (rail arrowheads now verified outside the terminal boxes: 506/507 vs box edges 514/515).

Per-diagram spec fixes (all validate 0/0, 9/9 showcase checks):

| diagram | fix |
|---|---|
| dao-cycle | all 8 titles back to 15 units (14.07 effective); 3 titles shortened per the hard column limit ("Settle epoch", "3-check gate", "Rollover") rather than shrinking; "Unclaimed" centered at its true midpoint; gate→rollover edge re-routed to merge with the claim→rollover riser (crossing eliminated, not papered over); boxes ≥8 from lane borders |
| hook-fee | "Volatility fee" / "Short-term fee" / "Dynamic fee" titles at 15 units (composition semantics moved to lane title "Dynamic fee = base fee + three dynamic components"); card 1 title → "The four components" |
| uasset-supply | Leveraged Genesis box 156→160 (title 14.9 → 14.83 effective); "Funding · interest" pad moved out of the Memeverse box corner; card orphan words rewritten; PSM asset list moved to the card, edge label "4 assets" on its line |
| omnichain-stages | west corridor rerouted x<270 with pixel-verified zero glyph intersections; Budget chip clear of the Queued border (+25px); legend wording → "Failure / exit (purple dashed)" |
| verse-lifecycle | at-deadline channel label pad lifted off the line (visible run, symmetric with the Fast Genesis channel) |
| yt-flash-buy/sell | legends unified byte-identical (request + "Message"); buy rows evened to 60px pitch mirroring sell; sell sublabel → "Sets min-receive floor" (back to 12.5 tier) |
| ecosystem-bite | demand-signal channel lowered (channelY 256): worst dead band 70px → 37px (schema floors prevented the full proposal) |

Post-fix audit: CSS font-size rules = 0 in all 13 SVGs; card titles contained in all 13; effective-size floors — min text 11.06–13.67, node-title tiers 13.82–17.08 (polend 13.82 stays the documented 1.3% canvas tradeoff, already accepted by the round-4 reviewer as imperceptible).
