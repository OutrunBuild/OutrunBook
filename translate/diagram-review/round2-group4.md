# Round 2 acceptance — yt-flash-buy, yt-flash-sell

Reviewer note: fresh pass; round-1 findings not consulted. Rendered at 820px (published size) and 1100px (detail) from assets/diagrams/*.svg. Facts checked against memeverse/yt-flash-swap.md.

## yt-flash-buy: PASS

Verified: title and message chain match the doc (sell y PT for R POL → put up y POL to split → repay with the split's y PT → receive y YT); cost "You actually pay y − R POL" correct; Split box "1 POL = 1 PT + 1 YT" correct; fact cards correct (max-pay cap, one fee on the full PT-leg size, Locked phase only, smart-account precondition, indicative quotes); "one atomic transaction" in title; legend styles (request / return / default message) match the arrow styles actually used (msg 1 emphasis solid, msg 2 default dashed, msgs 3–4 return dashed); all labels have mask backgrounds, no clipping, no overlaps, arrowheads land on lifelines, readable at 820 and 1100. Dark-grid family styling consistent with sell diagram.

- [P3] Empty band between the last message row ("You actually pay y − R POL", y≈348) and the Legend block (y≈426) leaves ~80px of dead space inside the lifeline frame → tighten viewBox height or move Legend up; cosmetic only.

## yt-flash-sell: PASS

Verified: message chain matches the doc (buy y PT for Q POL → merge y PT + your y YT → repay Q POL → receive y − Q POL); proceeds "y − Q POL" and "the larger Q, the less you net" correct; Merge box "1 PT + 1 YT = 1 POL" correct; fact cards correct (minimum-receive floor, one fee on full PT-leg, clean failure, one atomic execution, Locked phase only, smart-account precondition); same legend, palette, and card layout as buy — consistent family; no clipping, overlaps, or unreadable text at 820 or 1100.

- [P2] Delivery arrow "Receive y − Q POL" originates from the PT/POL pool lifeline, but per the doc the y POL are produced by the merge (step 2) with only Q owed to and repaid to the pool (step 3); the buy diagram correctly sources its delivery arrow from Split → source the sell delivery from Merge for factual accuracy and family symmetry.
