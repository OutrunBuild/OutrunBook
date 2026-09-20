# preorder-flow review (round 1)

Rendered and inspected at 820px and 1100px (`/tmp/diagram-png/preorder-flow-820.png`, `-1100.png`). SVG: `assets/diagrams/preorder-flow.svg` (viewBox 1080x640, embed scale 0.759 at 820px). Source: `assets/diagrams/src/preorder-flow.dataflow.json`. Truth: `memeverse/preorder.md`. Known global issues (label-chip white-on-white, gray-text dimness) excluded.

## P1

- [字体] At the 820px embed width every text tier collapses: node sublabels and tags are `font-size: 7` → ~5.3px effective ("Fixed 1% settlement fee", "Same launch transaction", "LP 65% / protocol 35%", "Stays claimable"), flow chips 8 → ~6.1px, stage headers 9 → ~6.8px, node labels 10 → ~7.6px, legend items 10 → ~7.6px. Sublabels/tags are below any readable floor, and they carry the core facts (1%, 65/35, linear unlock). → Export script should scale fonts up for a 1080-wide canvas (or emit a smaller viewBox); src JSON `viewBox` is the contributing half.

- [颜色搭配] Tag "LP 65% / protocol 35%" is teal `rgb(52,211,153)` (`text.t-backend[data-detail]`) painted on the green backend node fill — teal-on-green, lowest-contrast text on the canvas, and it holds the 65/35 split. Distinct from the known gray-dim issue (different class and fill). At 820px it is effectively invisible; at 1100px barely legible. → Export script: use the node-title color (or a dark-ink accent) for `fine`-detail text on filled nodes, not the node's own hue.

- [图形错误] Sigil icon collides with the label on "Pro rata by funds": icon at `translate(695 134)` (x≈695–704) sits directly on the "P" (label is center-anchored at x=745, ~102 units wide → spans ≈694–796). "Linear unlock" and "Aggregated buy" icons also touch the first glyph. Visible in both renders. → Export script: place the sigil outside the center-anchored label's measured width (left-align label next to icon for long labels), or shrink/offset the sigil.

- [产品语义] "Refunded in full" node is staged in lane "02 / Launch transaction" (`refund` stage 1, rect x259–371 → lane center 315). Per preorder.md the refund triggers when "Genesis ultimately falls short of its target" — the launch transaction never happens in that branch (the diagram's own second failure path, "Launch reverts", is correctly in lane 03). Placement asserts the refund occurs during launch. → src JSON: move `refund` to stage 0 ("Genesis", row 3 is free) or a dedicated pre-launch lane.

- [图形错误] Legend mislabels the failure edges: both dashed purple edges (`users-refund` "Genesis below threshold", `agg-rollback` "Cannot execute in full") are failure semantics, but legend kind `dashed` is auto-labeled "async batch"; meanwhile the legend's red "Failure branch" (`a-security`) matches zero edges in the diagram. A reader following the legend classifies the refund path as async batch. → Export script: derive legend labels from diagram semantics (or let src JSON override the `dashed` entry, as it already does for `security`); src JSON fix works only if `legend.entries` supports a `dashed` key.

- [产品语义] The three detail cards — "Capacity and basis" (capacity formula `(standard Genesis capital + leverage debt principal) × 70% × ratio`), "The fee rate is fixed" (1% details, 65/35, no referral rebate), "Failure and retention" — exist only in the HTML (`<h3>` markup), not in the SVG. preorder.md embeds the SVG directly (`![...](../assets/diagrams/preorder-flow.svg)`), so docs readers never see any of this content; the SVG alone also never states the capacity rule. → Export script: render cards inside the SVG (extend viewBox or a bottom band); src JSON alternative: promote the one-line capacity formula into a node sublabel/tag.

## P2

- [排列布局] `pool-first` and `agg-buy` terminate at the identical point (474,271) on Aggregated buy's left edge and overlap along x=422.5→474 (gray 1.4px drawn over green 1.8px); `pool-first`'s own arrowhead is completely hidden under the emphasis arrowhead, so "After primary pool created" visually dead-ends into the green flow instead of pointing at the node. → src JSON: route `pool-first` into the top edge (`toSide: "top"`, e.g. via x≈500) or give it a distinct entry y.

- [产品语义] Stages "02 / Launch transaction" and "03 / Aggregated settlement" split one atomic transaction into two sequential columns; per preorder.md settlement and pool creation share the launch tx. Mitigated by the "Same launch transaction" sublabel, but the column order still implies two txes. → src JSON: rename lane 03 (e.g. "Aggregated settlement · same tx") or place `aggregate` in lane 02 with lane 03 starting at distribution.

- [图例] Emphasis edge auto-labeled "primary data" — meaningless for a funds flow, and near-duplicate of the adjacent "Funds & flow" entry (the emphasis edge IS the funds flow). → src JSON: add a legend entry overriding the `emphasis` kind (e.g. "Preorder funds flow"), else export script.

- [排列布局] `dist-vest` path is degenerate (`M 745 186 L 745 186 L 745 356 L 745 356`, duplicated endpoints) — no visible artifact today, but brittle for any future marker/label math keyed to segment direction. → Export script: drop collinear duplicate composition points.

Not reported per instructions: blank white label chips ("After primary pool created", "Memecoin bought", "Escrowed", "Gradually claimable" — white-on-white exporter bug), dim gray text. Numbers verified against preorder.md: fixed 1% fee, LP 65% / protocol 35%, pro-rata by funds, shared average result, linear unlock with protocol-set duration, refund in full to preorder record beneficiary — all correct in the SVG.
