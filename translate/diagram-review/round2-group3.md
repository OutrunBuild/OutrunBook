# Round 2 acceptance — group 3 (uasset-supply, omnichain-stages, ecosystem-bite)

Fresh reviewer; round-1 findings not consulted. Rendered at 820px via /tmp/render-diagram.py (2x DPI); uasset-supply additionally at 1100px. Facts checked against outstake/uasset.md, outstake/README.md, memeverse/omnichain.md, README.md, ecosystem/flywheel.md. Edge semantics verified from `data-edge-from/to/label` attributes in the SVG sources.

Note for renderer users: /tmp/render-diagram.py writes a shared `/tmp/diagram-png/_diagram.svg` + `_wrapper.html`; concurrent renders clobber each other (my first omnichain render came back as fee-split content). Re-render serially or with renamed temp files before trusting a PNG.

## uasset-supply: PASS

All facts match outstake/uasset.md: three supply paths (Genesis Staking mint at face value from yield assets; PSM two-way 1:1 at par from USDC/USDT/ETH/BNB; leveraged Genesis quota minted as uAsset), uAsset = UETH/UUSD/UBNB pegged stablecoin, mint caps on position managers and PSM pools with redemption releasing room, destinations (Memeverse Genesis funding / leverage interest / settlement unit; USR savings earn interest, withdraw anytime), LayerZero circulation. Legend (primary data / data store / data flow) matches node styling (purple uAsset = data store). No overlaps, clipped labels, or arrows through text at 820px; footnote boxes legible.

Nitpicks (non-blocking):
- [P3] "Mint at face value" appears twice — as the top edge label and as the Genesis Staking node subtitle; redundant.
- [P3] uAsset→Memeverse and uAsset→USR savings edges exit uAsset's right side at the same y, so the green horizontal run is overdrawn by the gray edge until they split (~80px); color only differentiates after the split. Cosmetic.
- [P3] Footnote wrap "PSM swaps do / not" leaves "not" alone on a line.

## omnichain-stages: PASS

State machine matches memeverse/omnichain.md line by line (incl. the failure table): Send (source chain, exact fee) → Arrival (destination mints) → Placement (stakes into YieldVault) → Staking succeeds (verify shares). Failure edges verified in SVG source, all correct: send→revert "Fee inexact / below minimum unit" (funds do not move); send→receive "Non-integer multiple: truncated, remainder refunded"; receive→queued "Can't receive yet" (no rollback, redelivered); receive→stuck "Budget too low (extremely rare)" → Burned, not minted (stranded, manual recovery); settle→bare "YieldVault does not exist" → bare tokens, no shares or voting power, retry once vault is in place; placement fails → reverts, retriable. Legend (start/active/waiting/terminal success/failure) matches all node colors. Section grouping (stages / waiting and retries / degraded and stranded exits) is coherent; the busier bottom-left corner (Can't-receive-yet edge above Transaction reverts, fee-inexact arrow into it) stays clear of all text at 820px.

Nitpicks (non-blocking):
- [P3] "Placement fails / Reverts; can be retried" edge label sits directly above the Placement-reverts node whose subtitle repeats "Reverts; can be retried" — duplicated text.
- [P3] "extremely rare" (label + footnote) vs chapter's "In rare cases" — slightly stronger claim than the source.

## ecosystem-bite: PASS

Matches README.md and ecosystem/flywheel.md: OutStake supply side (multi-protocol yield assets wstETH/sUSDS/sUSDe…) → Mint uAsset (Genesis Staking · PSM) → uAsset (UETH/UUSD/UBNB, lifeline between modules) → Memeverse use side (4 pools · leverage · Staking · DAO), with the dashed demand-signal return labeled "Two-way supply-demand interlock (yields do not flow back)" and legend entry "demand signal — no yields flow back" — exactly the flywheel's use-drives-supply / independent-yield-loops framing. Edge labels "Genesis funding · leverage interest · settlement denomination" and "mint" match. Footnote boxes (interlock, yields don't flow back, the uAsset trio incl. LayerZero OFT) all consistent with sources. Clean at 820px; wide uAsset→Memeverse label clears the dashed return line below it.

Nitpicks (non-blocking):
- [P3] "Genesis Staking / PSM" edge label on supply→mint duplicates the Mint-uAsset node subtitle "Genesis Staking · PSM" (and uses "/" where the node uses "·").
