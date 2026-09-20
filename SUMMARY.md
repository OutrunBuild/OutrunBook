# Table of contents

> OutrunBook — the user-facing product documentation for the Outrun ecosystem. Written in English; protocol terms kept as-is.

---

## Overview

* [Outrun at a glance](README.md)
  — A two-module ecosystem: OutStake (yield infrastructure) + Memeverse (omnichain community consensus launcher), with uAsset as the lifeline connecting the two
* [Product vision](vision.md)
  — What Outrun sets out to solve, why these two modules, and the role of uAsset as a unified value medium

## OutStake — Yield infrastructure

* [OutStake at a glance](outstake/README.md)
  — Unifies yield-bearing assets from multiple protocols into the pegged stablecoin uAsset; includes "Why not just hold wstETH?"
* [SY standardized yield and the adapter matrix](outstake/sy-adapters.md)
  — Wraps the yield-bearing tokens of Aave/Lido/Sky/Ethena/Lista/Aster behind one standardized interface
* [uAsset pegged stablecoins](outstake/uasset.md)
  — The peg mechanism behind UETH/UUSD/UBNB, mint caps, and cross-chain circulation
* [Genesis Staking: minted for Memeverse](outstake/staking-modes.md)
  — Mint at face value with no interest, no liquidation, and no lock-up; your collateral keeps earning and the exposure stays yours
* [PSM par swaps](outstake/psm.md)
  — Two-way swaps between reserve assets and uAsset, 1:1 at par
* [USR savings](outstake/usr.md)
  — Deposit uAsset to earn interest; deposit and withdraw anytime
* [One-stop entry](outstake/router.md)
  — Aggregates the three routes that take any token into Genesis
* [Cross-chain and rate limits](outstake/omnichain.md)
  — Omnichain circulation of uAsset and its safety constraints

## Memeverse — Omnichain community consensus launcher

* [Memeverse at a glance](memeverse/README.md)
  — Launches not just a token, but an on-chain community with liquidity, yield, and governance
* [Launch lifecycle](memeverse/lifecycle.md)
  — The full flow from Genesis → lock-up/refund → unlock
* [Standard Genesis](memeverse/genesis.md)
  — uAsset principal conservation, the 24-hour liquidity protection, and the complete exit steps
* [The four-pool liquidity model](memeverse/four-pools.md)
  — Capital structure of the primary pool + three auxiliary pools, and where the fees go
* [Dynamic fee Hook](memeverse/hook.md)
  — A manipulation-resistant trading layer built on Uniswap V4 (EWVWAP exemption, anti-sandwich protection, pool-opening protection)
* [Preorder](memeverse/preorder.md)
  — Lock in a Memecoin ahead of Genesis, settle at a fixed rate, and unlock linearly
* [Leveraged Genesis POLend](memeverse/polend.md)
  — Pay interest to scale up your Genesis allocation, with no liquidation risk
* [POL split: PT and YT](memeverse/pol-splitter.md)
  — Splits POL into two tokens: principal (PT) and yield (YT)
* [YT Flash Swap](memeverse/yt-flash-swap.md)
  — Buy and sell YT with POL during the lock-up, reusing the PT/POL pools
* [GenesisCredit](memeverse/genesis-credit.md)
  — A cross-chain participation credit used to offset leverage interest
* [Memecoin Staking](memeverse/memecoin-staking.md)
  — Stake to earn trading fees; delegate to gain governance rights
* [Memecoin DAO governance](memeverse/dao-governance.md)
  — The community governs the treasury and the direction; vote to earn epoch rewards
* [Omnichain interoperability](memeverse/omnichain.md)
  — Multichain launches, cross-chain staking, and yield aggregation
* [vs Pump.fun](memeverse/vs-pump-fun.md)
  — A dimension-by-dimension mechanics comparison with Pump.fun

## Ecosystem — How the modules work together

* [Growth flywheel](ecosystem/flywheel.md)
  — The two-way interlock of uAsset supply and demand, plus an independent yield loop in each module (yields do not flow back and forth)
* [Participation and risk appetite](ecosystem/playbooks.md)
  — Conservative / Balanced / Co-build: three participation paths, with examples
* [Business model](ecosystem/business-model.md)
  — Revenue sources and the full path of a single trading fee
* [Target audience](ecosystem/audience.md)
  — What different roles need from the ecosystem, and how they take part

## Reference

* [Glossary](reference/glossary.md)
  — A quick reference for core terms
* [Participation map](reference/participation-map.md)
  — A master map of the three tiers × every mode, plus the POL/PT/YT payout timeline
* [FAQ](reference/faq.md)
  — Frequently asked questions
