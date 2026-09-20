# Round 2 acceptance — group 1 (fee-split, dao-cycle, hook-fee, preorder-flow)

Reviewer: fresh adversarial pass. Each diagram rendered at 820px embed width via Chromium (`/tmp/diagram-png/r2-*.png`), with zoomed crops for suspect labels. Semantics checked against the linked chapter only.

## fee-split: PASS

Rendered clean at 820px; all text legible, no overlap, no clipping, arrows route clearly around boxes.

Verified vs `ecosystem/business-model.md`:
- LP 65% / protocol 35% fixed; green "Main fee split" edges carry the `65% · fixed` / `35% · fixed` chips — matches "LPs take 65%, the protocol takes 35%".
- Referral rebate `Default 10% · adjustable`, fed by a "With referrer" edge FROM Protocol share (carved out of the 35%, not off the gross fee) — matches "referral rebate is carved out of the protocol's 35% (by default equal to 10% of the total fee)".
- Denomination routing: uAsset-denominated → DAO treasury (`0.25% to executor · default`); Memecoin-denominated → Staking YieldVault (For Memecoin stakers); POL-denominated → Burned directly (Deflationary). All three edge labels sit unambiguously on their own lines (zoom-verified) — matches chapter bullets.
- Aux-pool branch: edge `Auxiliary-pool POL/uAsset/PT fees (Locked)` into "Aux-pool split — rest to DAO treasury / Locked phase", then `Standard side: pro rata by Genesis share` → Genesis participants — matches the Locked-phase detail paragraph exactly.
- "Don't confuse the three treasuries" footnote matches the three-treasuries table (leverage interest → protocol treasury, not a trading fee).
- Legend (Main fee split / Treasuries / Funds and flows) consistent with usage.

No issues.

## dao-cycle: PASS

Rendered clean at 820px; legible, no overlap, no clipped labels.

Verified vs `memeverse/dao-governance.md`:
- `epoch 90 days · fixed` — matches "epoch (90 days, fixed)".
- Chain Stake shares → Delegate votes → Vote this epoch → Settle the epoch (`anyone; pays own gas`) — matches "someone must trigger settlement" + "all on-chain operations; you pay your own gas".
- 3-condition gate `enrolled/revenue/votes` with `All 3 hold` → Allocate rewards `25% default; adjustable`, and `One missing: full rollover` → Into treasury `allocated next epoch` with the purple dashed `Re-allocated next epoch` loop — matches settlement-conditions bullets and the rollover footnote.
- `In the window` → Active claim `your share of the votes` — matches active-claim bullet.
- Color legend (green = protocol actions, gray = user actions) applied consistently (settle/claim as user actions is fair since anyone triggers and pays gas).
- Footnote panels (voting power / undelegated shares raise quorum base / claim window, no reissue) all consistent with the chapter including the quorum note.

Notes (not FAIL):
- [Note] Large empty dark band (~20% of canvas height) between the legend and the footnote panels. Purely cosmetic dead space; nothing broken.

## hook-fee: PASS

Rendered clean at 820px; legible, no overlap.

Verified vs `memeverse/hook.md`:
- `Base fee 1% floor`, `+ adverse fee per address; 3s window`, `+ volatility fee per pool`, `+ short-term fee above 2%; 15s decay` — all match the component bullets.
- `Actual fee = max(dynamic fee, pool-opening decay fee)`, `cap 100% · fixed`, `Pool-opening fee 50%→1% in 15 min` — matches "hard cap of 100%" and "opening fee is 50%, decaying to 1% within 15 minutes; both are owner-adjustable defaults".
- EWVWAP exemption box: zoom-verified the subtitle renders as `history + reversal → 1%` (proper arrow glyph, not a broken character); dashed `Exempt: base fee only` edge into Actual fee — matches "Dynamic fee waived; only the base fee applies" and "first trade ... is not exempt".
- Footnotes: order-splitting defeated by 3s accumulation; decay-config-below-1% still floors at 1%; inside the decay window the higher of base fee vs current opening fee applies; normalized exponential decay — all match the chapter.

Notes (not FAIL):
- [Note] Same cosmetic blank band between legend and footnotes; section 03 panel has empty space left of the EWVWAP box.

## preorder-flow: PASS

Rendered clean at 820px; legible, no overlap; `Ledgered separately` zoom-verified (not truncated).

Verified vs `memeverse/preorder.md`:
- Preorder funds `First come, first served` / capacity footnote formula `(standard Genesis capital + leveraged debt principal) × 70% × protocol-configured ratio`, funds don't count toward the base — matches the chapter formula and bullets verbatim.
- `Genesis below threshold` → Refunded in full `Preorder beneficiary` — matches the example's refund-to-beneficiary.
- Primary pool `Same launch transaction` → `After primary pool created` → Aggregated buy `Fixed 1% settlement fee`; `Cannot execute in full` → Launch reverts `No partial settlement` — matches dedicated-channel, same-tx, and all-or-revert paragraphs.
- `Memecoin bought` → Pro rata by funds `Shared average result` → `Escrowed` → Linear unlock `Protocol-set duration` → `Gradually claimable` → Active claim `Stays claimable` — matches pro-rata distribution, linear unlock, self-claim retention.
- Legend line styles (green funds flow / dashed failure / gray funds & flow) used consistently.

Notes (not FAIL):
- [Note] Aggregated-buy box states `LP 65% / protocol 35%` and the footnote adds "not eligible for referral rebate". Not stated in preorder.md or hook.md for the dedicated channel; consistent with hook.md's fixed-split table but unverifiable from these chapters. Flag to a domain owner if the split for the dedicated channel is documented elsewhere.
