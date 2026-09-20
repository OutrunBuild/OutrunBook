# Round 2 acceptance — Group 2 (four-pools, genesis-rights, verse-lifecycle, polend-settlement)

Reviewer: fresh adversarial pass. Each SVG rendered via headless Chromium at 820px (publication width), polend-settlement additionally at 1100px, and compared against its chapter.

## four-pools: PASS

Verified vs memeverse/four-pools.md:
- ~70% primary / ~30% auxiliary split matches "about 70% ... remaining 30%".
- POL split 2:3:2 rendered as ~3/7 → Split PT + YT, ~2/7 → POL/uAsset pool, ~2/7 → PT/POL pool (sums to 1, matches "roughly 2:3:2").
- PT split 1:2 rendered as PT ~1/3 → PT/uAsset pool, PT ~2/3 → PT/POL pool.
- Note cards match: pool funding = standard capital + leverage debt principal, Preorder excluded and used for the first aggregated buy; leftover uAsset → settlement reserve (excess → treasury), leftover Memecoin burned, unused POL/PT claimed pro rata after unlock; 365-day liquidity lock.
- All labels legible at 820px; no overlaps, no arrow-through-text, legend matches node colors.

No issues.

## genesis-rights: PASS

Verified vs memeverse/genesis.md:
- Rights timing matches: Initial YT claimable from Locked (pro rata on success); Auxiliary-pool fee share accrues from Locked onward; Auxiliary-pool LP + residual POL/PT one-time claim after Unlocked.
- Conservation anchor "30% + 30% + 40% = 100%" matches the principal-source table.
- Window start = "transaction that enters Unlocked" (not scheduled time) matches; 365-day lock and 24-hour fixed window match; pools pause public trading while claims/redemptions run at static reserves; exit risk after window on the user — all match.
- All text legible at 820px; lanes, arrows and labels clean; legend (Genesis rights / Lifecycle) matches arrow styles.

No issues.

## verse-lifecycle: PASS

Verified vs memeverse/lifecycle.md:
- Main track Genesis → Locked (365 days · fixed, four pools deployed) → Unlocked (unified settlement) → Steady state (terminal) matches.
- Threshold rule rendered correctly: standard capital and leverage interest each compared independently, never added; Preorder funds and leverage debt principal excluded — matches "How Genesis meets its threshold".
- Fast Genesis early trigger vs at-deadline trigger; Refund exit ("After deadline, neither threshold met" → three fund classes refunded) matches the Refund section.
- Protection window 24h · pools paused, opens after settlement, auto-resume with public trading resuming — matches; unlock time = Genesis deadline + 365 days consistent with the fixed lock.
- Legend states (start/active/waiting/terminal success/failure-exit) match node colors; text legible at 820px, no overlaps.

No issues.

## polend-settlement: FAIL

Verified vs memeverse/polend.md — the settlement logic itself is faithful: atomic unlock (any step fails → whole reverts, stays Locked, retried after reserve replenished), recovery from auxiliary pools (burn POL; PT → uAsset), debt repaid first, surplus pro rata to interest, leveraged YT pro rata to interest, shortfall covered by settlement reserve at rounding level only, reserve replenish (cap may be raised) then retry, protection window 24 hours. Logic: no factual errors found.

- [P1] Node titles wider than their boxes on the three right-column nodes: "Protection window", "One-time residual", "Replenish reserve" — title glyphs start flush at the left border and the final glyph crosses/overlaps the right border stroke ("Replenish reserve" final "e" and "Protection window" final "w" sit half on the border). Visible at 820px (worst of the three at both 820 and 1100px: Replenish reserve). Boxes are 110 SVG units wide but the 17-char semibold titles render ~108+ units → zero padding. → Widen those boxes (or drop node title font-size ~1px) so titles keep >= 8 units side padding; same check for "Unified settlement" (18 chars in a 120-unit box) which is near-zero padding.
- [P2] ~120 SVG units of empty vertical space between the Legend row and the three note cards (viewBox height 740; content ends ~y620). Not a defect at the FAIL bar, but the gap reads as a layout accident in the published doc. → Tighten viewBox height or move notes up.
- [P2] Note-card wording "uAsset fees go to the protocol treasury" conflicts with sibling chapters: memeverse/memecoin-staking.md routes the uAsset-denominated fee portion to the **DAO treasury**, and four-pools.md sends post-unlock accrued fees to the **DAO treasury** (polend.md itself reserves "protocol treasury" for leverage interest, distinct from the DAO treasury). polend.md does not cover captured-fee routing, so the author should confirm which treasury is meant; if DAO treasury, the diagram is wrong.
