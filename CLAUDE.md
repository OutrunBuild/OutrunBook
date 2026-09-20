# CLAUDE.md — OutrunBook

OutrunBook is the Outrun ecosystem's **user-facing product documentation (English edition of the Chinese original)** (GitBook structure), not a contract API / technical reference. It covers "what you can do, what you get, and why," not code implementation.

## Repository relationships and the code source of truth

The documentation's content is grounded in the two sibling Foundry repositories; **before changing any mechanism description, you must defer to the code / spec**:

| Repository | Path | Role | Docs-aligned commit |
|---|---|---|---|
| **MemeverseV2** | `/home/azkrale/Web3Project/Memeverse` | Omnichain community consensus launcher (four pools / Hook / POLend / POLSplitter / YieldVault / DAO / cross-chain). The on-disk directory was originally named MemeverseV2 and has been renamed | `3cdb8046380bf1af8ae57a04be5e92c086834567`(`3cdb804`, feat(polend): expose marketUAsset getter and cover payer/user separation) |
| **OutStakeV2** | `/home/azkrale/Web3Project/OutStake` | Yield infrastructure (SY adapters / uAsset / CDP positions / PSM / USR / cross-chain). The on-disk directory was originally named OutStakeV2 and has been renamed | `73c9b1637c4953dad99fb702cf0c4fbda3150997`(`73c9b16`, chore(harness): refresh policy surfaces and lint/slither baselines) |

> When the code repositories are updated, update the commit hashes here and re-verify that the documentation still aligns. Before publishing, run `bash scripts/check-baseline.sh` to detect drift and `bash scripts/check-absolute-words.sh` to check absolute marketing words. Every occurrence must carry an on-chain constraint or a qualifier. For new hits, verify first, then decide whether to change the docs or add them to the whitelist.

### MemeverseV2 source-of-truth documents (read these first; closer to design intent than the code)

- `docs/spec/protocol.md`, `docs/spec/verse/accounting.md`, `docs/spec/verse/config-matrix.md`
- `docs/spec/polend/core.md`, `genesis.md`, `settlement-and-fees.md`, `pt-yt-splitter.md`
- `docs/spec/governance/governance-yield-details.md`, `docs/spec/swap/swap-flow.md`, `yt-flash-swap.md`
- `docs/ARCHITECTURE.md`, `docs/GLOSSARY.md`
- OutStakeV2 (on-disk directory name `OutStake`) has specs: `docs/spec/protocol.md`, `common-foundations.md`, `access-control.md`, `position/state-machines.md`, `position/accounting.md`, `router/router-and-user-flows.md`, `yield/yield-adapters.md`, `yield/oracles-and-integrations.md`; the code's NatSpec is secondary.

## Writing rules (explicitly requested by the user; must be followed)

1. **User-facing product language**: must not contain function names (`stake()`), variable names (`amountInSY`), line numbers, code formulas, or "Code Reference" sections. Do not introduce overly technical phrasing; readability of the docs comes first.
2. **Chinese punctuation**: in Chinese-language contexts use full-width punctuation (，。：；！？（）), except in special cases (code, URLs, ratios between numbers such as `2:3:2`, and inside English terms). Punctuation after English terms such as `Memeverse`/`YT`/`DAO` is also Chinese punctuation. This rule applies to the Chinese edition; the English edition uses standard English punctuation.
3. **Terms stay in English**: uAsset / SY / PT / YT / POL / Hook / POLend / Preorder / GenesisCredit / YieldVault, etc., are never translated.
4. **Examples**: use "a user" / role names; **never use fictional personal names** (Laowang/Xiaoli). For Memecoin examples use the generic "Memecoin"; **never a specific ticker** (FROGGY).
5. **Uniform template for user-operation pages**: every page that teaches users to perform an operation (Genesis, Preorder, staking, redemption, cross-chain, governance, etc.) covers the following fields in this order; when a field does not apply to that operation, **mark it explicitly "Not applicable" rather than omitting it**:
   - When it is available (in which phase / under what conditions the operation can be performed)
   - Inputs and outputs (what goes in, what comes back)
   - Prerequisite balances and approvals (what the wallet must hold beforehand, whether approval is required)
   - Fees and failure outcomes (which fees are charged, how funds are handled on failure or when conditions are not met; pause impacts are handled uniformly through FAQ cross-references, not repeated page by page)
   - Concrete steps (including steps the user must actively claim/execute; never write only that funds arrive automatically)

## Key mechanism decisions (all verified against the code or confirmed by the user; never overturn them when editing docs)

- **uAsset = pegged stablecoin** (UETH/UUSD/UBNB pegged to ETH/USD/BNB). UETH/UBNB peg volatile assets; they are not fiat stablecoins. At the code level it is a debt-tracked receipt; at the product level the stablecoin narrative applies; never call it a "debt receipt".
- **Flywheel = two-way interlock of uAsset supply and demand** (OutStake supplies ↔ Memeverse creates the demand), **not yield flowing back**. Each module's yield is independent; nothing flows back and forth between them.
- **Standard Genesis = no risk within the product model**: 100% of the committed uAsset goes into the four-pool portfolio; the Memecoin is newly minted upside on top of principal. After the Verse unlocks successfully, the four pools pause public trading for 24 hours. Within that window, standard Genesis participants must claim and fully unwind YT, auxiliary-pool LP, POL/PT residual, and fee claims to restore their uAsset principal pro rata. After the protection window, risk is on them. The mechanism rests on **principal conservation + unlock protection**, not on users directly holding PT principal certificates. The authoritative page is `memeverse/genesis.md`.
- **Fee flows**: trading fees LP 65% / protocol 35%; protocol fees denominated in uAsset → DAO treasury, in Memecoin → staking YieldVault, in POL → burned; with a referrer, 10% of the total fee → referral rebate; executor reward = 0.25% of primary-pool uAsset fees; leverage interest → protocol treasury (not the DAO treasury).
- **Three treasuries**: Memecoin staking YieldVault (stakers) / DAO treasury (uAsset fees, community governance) / protocol treasury (leverage interest, protocol side).
- **Four-pool ratios**: the primary pool (Memecoin/uAsset) takes 70% of genesis capital; POL split 2:3:2; PT take 1:2.
- **split/merge only during the Locked phase** (reverts after Unlocked/settled).
- **YT Flash Swap**: the secondary-market channel for YT during the lock-up period. A dedicated Router reuses the PT/POL pools (no second AMM, no separate YT pool) and completes the leg swap + split/merge within a single unlock. Two entries: POL→exact YT (actual cost settles at y−R; no budget is pre-deducted) and exact YT→POL (minPOLOut protection). Fees/referral work exactly as in a regular PT/POL swap (no double charging). However, the fee is computed on the full PT-leg size, so under leverage it is amplified relative to the principal actually paid. An active account session is required (atomically wrapped by the smart account, principal = msg.sender). Available only during the Locked phase. YT effective price = 1 POL − PT market price. **YT = leveraged asset**: pay a small fraction of the price for the full share of settlement residual-value exposure; a small move in the residual → a large move in YT returns (this matches Pendle's official "leveraged exposure to yield": buying YT = going long the settlement residual, amplified in both directions).
- **Three participation tiers**: Conservative (no risk) / Balanced (leverage, interest cost only) / Co-build (buy, stake, govern). The old name was "Aggressive"; the user found it unappealing, so it was renamed "Co-build".
- **OutStake position = the face-value minting layer reserved for Memeverse**: the only minting entry exists solely to fund Genesis; minted at face value; no interest, no liquidation, no lock-up; redeem anytime. The old dual staking (locked/wrapped), value extraction, and keeper repayment have been removed; never write them back.
- **PSM = the par swap pool backed by protocol reserves**: USDC/USDT for UUSD, ETH for UETH, BNB for UBNB, 1:1 at par in both directions, no position and no debt; fees default to ~0.1% each way (adjustable, capped at 1%); each pool has a net-mint cap.
- **USR = the uAsset savings layer**: suETH/suUSD/suBNB shares, with deposit and withdrawal anytime. The share price grows at the per-family rate; the rate is capped at 10% and defaults to 0 at launch (inactive). Interest is paid from a protocol-funded budget that pauses growth automatically when exhausted. The protocol side has no withdrawal path; it can only inject funds.
- **DAO**: standard token voting (staked Memecoin shares), not the old "sMemecoin+POL dual-track TVP formula" (no longer in the code).

## Document structure

```
README.md / vision.md / SUMMARY.md (table of contents)
outstake/    OutStake mechanism chapters
memeverse/   Memeverse mechanism chapters
ecosystem/   Flywheel / business model / audience / participation (playbooks)
reference/   Glossary / participation overview / FAQ
.claude/internal/gap-analysis.md   internal working notes (not in the public book)
```

- After editing docs, watch whole-book consistency (the same mechanism described in multiple places will drift, e.g. standard Genesis "no risk", the three-treasuries terminology).
- The punctuation batch-fix script approach is in the git history; **note**: the full-stop conversion must keep its "preceding character is CJK" precondition, otherwise list items `1.` would be wrongly converted to `1。`.
