# Dynamic fee hook

## Built on Uniswap V4

Memeverse does not build its own trading engine; its trading layer is built on **the Uniswap V4 hook mechanism**. Hooks let custom logic run before and after every swap. Memeverse uses them to implement dynamic fees, Preorder settlement, and short-term impact pricing, while the liquidity itself benefits from Uniswap V4's maturity and security.

## Components of the dynamic fee

A plain AMM has a single fixed fee tier, which arbitrageurs and high-frequency strategies can exploit. Memeverse's fee is **dynamic**: a base fee plus three dynamic components.

- **Base fee**: a floor of 1%.
- **Adverse impact fee (per address)**: when a trade pushes the price away from equilibrium, it is charged in proportion to the impact. Consecutive impacts from the same address within a 3-second window accumulate into one combined charge. Order-splitting attacks (breaking a large order into small ones to dodge the fee) therefore cannot escape impact costs: every split order counts toward the same window's accumulated impact.
- **Volatility fee (per pool)**: the more violent the pool's recent price swings, the higher the fee. This dampens excessive speculation.
- **Short-term impact fee (per pool)**: every trade is charged on its price impact; impact up to 2% is exempt (only the portion above 2% is charged). Impact decays over 15 seconds, and rapid consecutive impacts stack.

The fee has a hard cap of 100%; the cap is fixed, so the fee can never spike without limit.

<iframe src="../assets/diagrams/hook-fee.html" loading="lazy" style="width:100%;height:800px;border:1px solid #e5e7eb;border-radius:8px" title="How the actual fee is composed"></iframe>

## When fees are added, and when they are waived

Whether the dynamic fee applies, and by how much, is decided by these conditions:

| Trade condition | Fee |
|---|---|
| First trade (the pool has no trade history yet) | Full dynamic fee |
| Trade pushes the price away from equilibrium (EWVWAP) | Full dynamic fee |
| Trade brings the price back toward equilibrium, and the pool already has trade history | Dynamic fee waived; only the base fee applies |
| Accumulated impact from the same address within a 3-second window | Adverse impact fee accumulates |
| Rising price volatility in the pool | Volatility fee rises |
| A single trade's price impact exceeds 2% | Short-term impact fee charged on the excess (rapid consecutive impacts within 15 seconds stack) |

## The EWVWAP exemption: fees waived only in the right direction

The dynamic fee is not always friendly to ordinary users, but there is one key exemption. **When the pool already has trade history and a trade leaves the price closer to equilibrium (EWVWAP) than it was before the trade, all dynamic fees are skipped. Only the base fee is charged.**

This means:

- Trades that bring the price back toward equilibrium (including buying with the trend and providing liquidity) pay only the base fee. Inside the opening-fee decay window, the higher of the base fee and the current opening fee applies instead.
- Trades that push the price away from equilibrium and create volatility bear the dynamic fee under the conditions above.

Note: the first trade, which has no trade history, and any single trade that pushes the price away from equilibrium are both outside the exemption.

## High initial fee at pool open deters snipers

A pool is most fragile the moment it opens: snipers race to jump ahead of the first trade. Memeverse sets a **very high opening fee** at the instant the pool opens, then decays it exponentially over time down to the base fee. **By default the opening fee is 50%, decaying to 1% within 15 minutes; both are owner-adjustable defaults.** The fee decays over time, so the later you enter, the lower the fee.

With the default configuration, the fee decays roughly as follows after pool open (following a normalized exponential curve):

| Time after pool open | Opening fee |
|---|---|
| 0 minutes | 50% |
| 1 minute | ~38% |
| 5 minutes | ~13% |
| 10 minutes | ~3.6% |
| 15 minutes | 1% |

The two endpoint values (opening 50%, final 1%) are the current defaults and adjustable by the protocol; the intermediate values scale with the actual parameters.

## How the fee is split

Each swap's fee is split at fixed proportions:

| Scenario | LP | Protocol treasury | Referral rebate |
|---|---|---|---|
| No referrer | 65% | 35% | 0 |
| With referrer (default) | 65% | 25% | 10% |

The referral rebate comes out of the protocol's fee share; it rewards referrers who bring in new users and encourages the community to spread the word.

## Who can initiate a trade

All public trading on Memeverse is initiated by **smart accounts**. Plain wallets (accounts with no deployed contract code) cannot execute trades directly; a smart-account wallet such as Safe is required. The entire trade completes inside a single atomic transaction as "open session → execute the swap → close session". The frontend wraps the session automatically, and it is invisible to the user. If there is no active session, or the session initiator and the trade initiator are not the same wallet, the trade simply reverts, with no loss of funds.

This requirement matches [YT flash swap](yt-flash-swap.md) and is the uniform rule of Memeverse's trading layer.

## A dedicated settlement channel for Preorder

Preorders do not go through the public trading path. They settle through a **dedicated channel inside the hook with a fixed 1% fee** (see [Preorder](preorder.md)), bypassing both the dynamic fee and the pool-opening high-fee mechanism. All Preorder funds are aggregated into the first AMM trade after the primary pool is created, and the Memecoin received is distributed pro rata to each preorder's share of the funds. All Preorder participants share the average execution cost of that single trade; what is fixed is the settlement fee, not the Memecoin's unit price. This settlement shifts the primary pool's reserves and the starting price of the public trading that follows.

## Example

> A Memecoin has just opened its pool: the opening fee is 50%, decaying to 1% over 15 minutes. The first swap after open has no swap history, so it pays the full dynamic fee. A sandwich attacker then tries to sandwich a large order: its trades push the price away from equilibrium with a single-trade impact above 2%, so the adverse impact fee and the short-term impact fee are charged together. Conversely, as long as the pool already has trade history, a trend-following trade pointed back toward equilibrium triggers the EWVWAP exemption and pays only the base fee. Inside the opening-fee decay window, the higher of the base fee and the current opening fee applies.

## Pricing dimensions and their limits

The dynamic fee hook prices trades along three dimensions: direction, time window, and volatility. Trades that bring the price back toward equilibrium can pay as little as the base fee; trades that push the price away or create impact bear higher costs. This is how Memeverse's trading layer balances market depth with manipulation resistance. The dynamic fee is a **mitigation, not an absolute guarantee**: the actual fee and the protection it provides vary with the pool's state and the owner's configured parameters.
