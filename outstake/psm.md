# PSM par swaps: reserve assets straight into uAsset

The **PSM** (Peg Stability Module) is a reserve-backed par swap pool: you swap between reserve assets and uAsset in either direction **at par, 1:1**. Unlike [Genesis Staking](staking-modes.md), a swap settles on completion: no position left open, no debt taken on. uAsset is backed by reserve assets held by the protocol.

## The four swap pools

| You swap in | You get | Direction |
|---|---|---|
| USDC | UUSD | Both ways |
| USDT | UUSD | Both ways |
| ETH | UETH | Both ways |
| BNB | UBNB | Both ways |

The 1:1 is a relationship at **par**: you exchange reserve assets and uAsset of equal face value, and the only deduction on receipt is a small swap fee. No market price enters the exchange.

## How to swap

- **When it's available**: under normal conditions, any time. While a uAsset is temporarily paused, swaps in both directions are unavailable (see the [FAQ](../reference/faq.md)). When a single pool's net-mint cap is used up, the mint direction of that pool pauses and becomes available again automatically once capacity recovers.
- **Inputs and outputs**: reserve assets for uAsset, or uAsset for reserve assets. Each pool handles only its own asset pair (the USDC pool takes in and pays out only USDC and UUSD); assets cannot be mixed across pools.
- **Balance and approvals**: your wallet must hold enough of the asset you are swapping out. If the outgoing asset is an ERC20 (USDC, USDT, uAsset), confirm the spending approval first; native ETH and BNB require no approval.
- **Fees and failure handling**: each direction charges a small swap fee (currently about 0.1% each way by default, adjustable and capped at 1%; the interface display is authoritative). The fee stays in the pool and goes to the protocol. You pay on-chain gas and nothing else. The whole transaction reverts, with no loss of funds, in three cases: the cap is exhausted; the pool's reserves run short; or the input is too small (for example, a dust amount reduced to zero by the fee).
- **Steps**: choose a pool and direction → confirm the approval (if needed) → submit the swap → receive the assets (you can check the quote before submitting; the quote matches execution).

## What to use it for

- **Funding Genesis**: if you hold only USDC, ETH, or BNB, swap into uAsset in one step and go straight into a Memeverse Genesis, without first finding a yield-bearing asset.
- **Day-to-day conversions**: move between uAsset and reserve assets at par. For anyone who uses uAsset as a stablecoin.
- **Peg arbitrage**: when uAsset trades above par, swap it out for a profit; when it trades below par, buy in and swap it back for reserve assets. This two-way arbitrage keeps uAsset close to its peg over time.

Holding a yield-bearing asset and want uAsset while it keeps earning as collateral? Use [Genesis Staking](staking-modes.md). Already have uAsset and want it to earn interest? See [USR savings](usr.md).
